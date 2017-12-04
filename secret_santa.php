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
*/

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
	}
}
$random = new uRandom;
$random->Fire();
?>
