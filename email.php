<?php
class Contact{
    var $firstname;
    var $lastname;
    var $mail;
    var $to_send;
};

	$data = array();

    $obj = new Contact();
    $obj->firstname = 'First name';
    $obj->lastname  = 'Last name';
    $obj->mail      = 'mail';
    $obj->to_send	= true;
    array_push($data, $obj);
   
    $obj2 = new Contact();
    $obj2->firstname = 'First name';
    $obj2->lastname  = 'Last name';
    $obj2->mail      = 'mail';
    $obj2->to_send	= false;
	array_push($data, $obj2);
    
    echo json_encode($data);