<?php
use PHPMailer\PHPMailer\PHPMailer;
class checkandemail
{
    private function cryptocompare($coin)
    {
        $url = "https://min-api.cryptocompare.com/data/price?fsym=".$coin."&tsyms=SGD";
        $response = $this->curl_link($url);
        if (array_key_exists('Response', $response))
        {
            error_log($url.' returned an error');
        }
        else
        {
            $floatvalue = floatval($response['SGD']);
            return $floatvalue;
        }
    }

    private function coinmarketcap($ticker)
    {
       $url = "https://api.coinmarketcap.com/v1/ticker/".$ticker."/";
       $response = $this->curl_link($url);
       return $response;
    }

    public function fire()
    {
        $symbolarray = array('LTC','ETH');
        foreach ($symbolarray as $arr)
        {
            $price = $this->cryptocompare($arr);
            if ($arr == "ETH" && floatval($price) < 340 && floatval($price) > 450) 
            {
                $message = "This message is being sent to you became there is a significant shift in ETH.\r\n";
                $message .= "While we appreciate that you are enjoying your holiday in bangkok, this is something you might want to take note of.\r\n";
                $message .= "ETH has now hit a trigger point of ".$price."\r\n";
                $message .= "\r\n";
                $message .= "With regards,\r\n";
                $message .= "Hermes (Email Variant)\r\n";
                $message .= "<i>This script is configured to alert users when prices are currently at a 7% hourly difference.</i>\r\n";
                $message .= "<i>This script is configured to alert users when ETH prices drop below 340 or rise above 450</i>\r\n";
                $message .= "<i>This script runs on a 5 minutes interval.</i>\r\n";
                $message .= "<i>To stop it from emailing you, text me</i>";
                $title = "Swing in price of ETH";
                $this->sendmail($title,$message);
            }
            else if ($arr == "LTC" && floatval($price) <= 60 && floatval($price) >= 90)
            {
                $message = "This message is being sent to you became there is a significant shift in ETH.\r\n";
                $message .= "While we appreciate that you are enjoying your holiday in bangkok, this is something you might want to take note of.\r\n";
                $message .= "LTC has now hit a trigger point of ".$price."\r\n";
                $message .= "\r\n";
                $message .= "With regards,\r\n";
                $message .= "Hermes (Email Variant)\r\n";
                $message .= "<i>This script is configured to alert users when prices are currently at a 7% hourly difference.</i>\r\n";
                $message .= "<i>This script is configured to alert users when ETH prices drop below 340 or rise above 450</i>\r\n";
                $message .= "<i>This script runs on a 5 minutes interval.</i>\r\n";
                $message .= "<i>To stop it from emailing you, text me</i>";
                $title = "Swing in price of LTC";
                $this->sendmail($title,$message);
            }
        }
        $cmcarray = array('ethereum','litecoin');
        foreach ($cmcarray as $cmc)
        {
           $response = $this->coinmarketcap($cmc);
           $percent_change_1h = $response[0]['percent_change_1h'];
           $percent_change_24h = $response[0]['percent_change_24h'];
           if (floatval($percent_change_1h) > 7 || floatval($percent_change_1h) < -7)
           {
                $message = "This message is being sent to you became there is a significant shift in ".$cmc." of <b>7%</b> within the last hour.\r\n";
                $message .= "While we appreciate that you are enjoying your holiday in bangkok, this is something you might want to take note off.\r\n";
                $message .= $cmc." experienced a ".$percent_change_1h." change within the last hour\r\n";
                $message .= "For reference, ".$cmc." had a swing of ".$percent_change_24h." in the last 24 hours\r\n";
                $message .= "\r\n";
                $message .= "With regards,\r\n";
                $message .= "Hermes (Email Variant)\r\n";
                $message .= "<i>This script is configured to only alert users when prices are currently at a 7% hourly difference.</i>\r\n";
                $message .= "<i>This script runs on a 5 minutes interval.</i>\r\n";
                $message .= "<i>To stop it from emailing you, text me</i>";
                $title = "Swing in price of ".$cmc;
                $this->sendmail($title,$message);
           }
        }

    }

   

    private function curl_link($url)
    {
        $cURL = curl_init();
        curl_setopt($cURL, CURLOPT_URL, $url);
        curl_setopt($cURL, CURLOPT_HTTPGET, true);
        curl_setopt($cURL, CURLOPT_HTTPHEADER, array(
            'Content-Type: application/json',
            'Accept: application/json'
        ));
        curl_setopt($cURL, CURLOPT_RETURNTRANSFER, true);

        $result = curl_exec($cURL);
        $response = json_decode($result, true);
        curl_close($cURL);
        return $response;
    }

    private function sendmail($title,$message)
    {
        require 'vendor/autoload.php';
        $mail = new PHPMailer;
        $mail->isSMTP();
        $mail->SMTPDebug = 2;
        $mail->Host = 'smtp.gmail.com';
        $mail->Port = 587;
        $mail->SMTPSecure = 'tls';
        $mail->SMTPAuth = true;
        $mail->Username = "email";
        $mail->Password = "password";
        $mail->setFrom('email', 'Jingkai Tan');
        $mail->addAddress('email', 'Jingkai Tan');
        $mail->Subject   = $title;
        $mail->Body = $message;
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

ini_set("log_errors", 1);
error_reporting(E_ALL); 
ini_set("error_log", date('Y-m-d')."email_script.log");
date_default_timezone_set("UTC");
$emailclass = new checkandemail;
$emailclass->fire();
?>
