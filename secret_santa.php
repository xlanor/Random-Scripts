<?php
/*
Pulls from a mySQL database and assigns each user a secret santa
DB Structure
===================================
              db.User
===================================
user_idIndex	int(11) NULL AUTO_INCREMENT UNIQUE
user_name	varchar(50)	
received_status	varchar(11)	
given_status	varchar(50)
from_user	int(11)	NULL
received_user	int(11)	NULL
email varchar(100)
====================================
    Default initalized values
====================================
received_status = Unexchanged
given_status = No
*/
use PHPMailer\PHPMailer\PHPMailer;
class uRandom
{
	private function getToFromDB(){
		include('connection.php');
		$userarray = array();
		$selectq = "SELECT * FROM user WHERE given_status = 'No'";
		$selectx = $dbh->prepare($selectq);
		$selectx->execute();
		if($selectx->rowCount() > 0){
			$fetch = $selectx->fetchAll();
			foreach($fetch as $fetched){
				array_push($userarray,$fetched['user_id']);
			}
		}
		return $userarray;
	}
	private function getFromFromDB(){
		include('connection.php');
		$userarray = array();
		$selectq = "SELECT * FROM user WHERE received_status ='Unexchanged'";
		$selectx = $dbh->prepare($selectq);
		$selectx->execute();
		if($selectx->rowCount() > 0){
			$fetch = $selectx->fetchAll();
			foreach($fetch as $fetched){
				array_push($userarray,$fetched['user_id']);
			}
		}
		return $userarray;
	}
	private function RandomNumber(){
		$from_done_array = array();
		$to_done_array = array();
		$fromarray = $this->getFromFromDB();
		$toarray = $this->getToFromDB();
		$fromlength = count($fromarray);
		$tolength = count($toarray);
		$countfromlegnth = $fromlength-1;
		$counttolength = $tolength-1;
		$counttrigger = True;
		while($counttrigger){
			if($fromlength == 0){
				$counttrigger = False;
			}else{
				$random_from = random_int(0, $countfromlegnth);
				$random_to = random_int(0,$counttolength);
				if($random_from != $random_to){
					if(!in_array($random_from, $from_done_array)){
						if(!in_array($random_to, $to_done_array)){
							$this->updateDB($toarray[$random_to],$fromarray[$random_from]);
							print($fromarray[$random_from].' '.$toarray[$random_to]).PHP_EOL;
							array_push($from_done_array,$random_from);
							array_push($to_done_array,$random_to);
							unset($fromarray[$random_from]);
							unset($toarray[$random_to]);
							$fromlength = $fromlength -1;

						}
					}
				}
					
				
			}
		}
		echo "All generated".PHP_EOL;
		

	}
	private function UpdateDB($user_id,$from){
		include('connection.php');
		$updatetouserq = "UPDATE user SET received_status = 'Received', from_user = :fu WHERE user_id = :tou";
		$updatetouserx = $dbh->prepare($updatetouserq);
		$updatetouserx->bindParam(':fu',$from);
		$updatetouserx->bindParam(':tou',$user_id);
		$updatetouserx->execute();
		$updatefromuserq = "UPDATE user SET given_status = 'Yes', received_user = :ru WHERE user_id = :frou";
		$updatefromuserx = $dbh->prepare($updatefromuserq);
		$updatefromuserx->bindParam(':ru',$user_id);
		$updatefromuserx->bindParam(':frou',$from);
		$updatefromuserx->execute();
	}
	private function CheckDB(){
		include('connection.php');
		$selectq = "SELECT * FROM user";
		$selectx = $dbh->prepare($selectq);
		$selectx->execute();
		if($selectx->rowCount() > 0)
		{
			$fetch = $selectx->fetchAll();
			foreach($fetch as $fetched){
				if($fetched['from_user'] == $fetched['received_user']){
					$clearq = "UPDATE user SET received_status = 'Unexchanged', given_status = 'No', from_user = '0', received_user = '0'";
					$clearx = $dbh->prepare($clearq);
					$clearx->execute();
					return False;
				}
			}
		}
		return True;
	}
	
	private function generateEmailList(){
		include('connection.php');
		$userarray = array();
		$selectq = "SELECT a.user_name, a.email, 
					b.user_name AS to_user, 
					c.user_name AS from_user 
					FROM `user` a INNER JOIN user b ON a.user_id = b.from_user 
					INNER JOIN user c ON a.user_id = c.received_user";
		$selectx = $dbh->prepare($selectq);
		$selectx->execute();
		if($selectx->rowCount() > 0){
			$fetch = $selectx->fetchAll();
			foreach($fetch as $fetched){
				array_push($userarray,array("name"=>$fetched['user_name'],"email"=>$fetched['email'],"give_to"=>$fetched['to_user']));
			}
		}
		return $userarray;
	}
	private function fireMail($userarray){
		require '../randomscripts/vendor/autoload.php';
		foreach ($userarray as $user){
			$title = "Secret Santa assignment for ".$user['name'];
			$message = "Good Morning/Afternoon/Evening ".$user['name']."\r\n";
			$message .= "You have been assigned as the secret santa of ".$user['give_to']."\r\n";
			$message .= "Regards, \r\n";
			$message .= "Santa Script";
			$mail = new PHPMailer;
			$mail->isSMTP();
			$mail->SMTPDebug = 2;
			$mail->Host = 'smtp.gmail.com';
			$mail->Port = 587;
			$mail->SMTPSecure = 'tls';
			$mail->SMTPAuth = true;
			$mail->Username = "youremail";
			$mail->Password = "yourpassword";
			$mail->setFrom('youremail', 'Santa Script');

			$mail->addReplyTo('youremail', 'yourname');
			$mail->addAddress($user['email'], $user['name']);
			$mail->Subject = $title;
			$mail->Body= $message;
			if (!$mail->send()) 
			{
				error_log("Mailer Error: " . $mail->ErrorInfo);
			} 
			else 
			{
				error_log("Message sent!");
			   
			}
		}
	
	}
	
	public function Fire(){
		$this->RandomNumber();
		$sentinel = True;
		while($sentinel){
			if(!$this->CheckDB()){
				echo 'Duplicate found'.PHP_EOL;
				$this->RandomNumber();
			}else{
				$sentinel = False;
			}
		}
		$userarr = $this->generateEmailList();
		$this->fireMail($userarr);
	}

}
$random = new uRandom;
$random->Fire();
?>
