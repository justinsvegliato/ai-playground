(define (problem complex_delivery)

(:domain world)

(:objects 
    jackal - robot
    shlomo-mail joydeep-mail lpr-mail amrl-mail rbr-mail - mail
    shlomo-office joydeep-office lpr amrl rbr lobby stairwellA stairwellB - location 
)

(:init
    (at shlomo-mail shlomo-office)
    (at joydeep-mail joydeep-office)
    (at lpr-mail lpr)
    (at amrl-mail amrl)
    (at rbr-mail rbr)
    (at jackal amrl)
    
    (= (distance amrl rbr) 10)
    (= (distance amrl lpr) 10)
    (= (distance rbr amrl) 10)
    (= (distance rbr stairwellA) 20)
    (= (distance stairwellA shlomo-office) 10)
    (= (distance shlomo-office stairwellA) 10)
    (= (distance shlomo-office lobby) 50)
    (= (distance lobby shlomo-office) 50)
    (= (distance lobby joydeep-office) 40)
    (= (distance lobby lpr) 20)
    (= (distance joydeep-office lobby) 40)
    (= (distance joydeep-office stairwellB) 10)
    (= (distance stairwellB joydeep-office) 10)
    (= (distance stairwellB lobby) 50)
    (= (distance lpr lobby) 20)
    (= (distance lpr amrl) 10)
    
    (connected amrl rbr)
    (connected amrl lpr)
    (connected rbr amrl)
    (connected rbr stairwellA)
    (connected stairwellA shlomo-office)
    (connected shlomo-office stairwellA)
    (connected shlomo-office lobby)
    (connected lobby shlomo-office)
    (connected lobby joydeep-office)
    (connected lobby lpr)
    (connected joydeep-office lobby)
    (connected joydeep-office stairwellB)
    (connected stairwellB joydeep-office)
    (connected stairwellB lobby)
    (connected lpr lobby)
    (connected lpr amrl)
    
    (= (total_distance_travelled) 0)
)

(:goal
    (and (forall (?x - mail) (has jackal ?x))
         (at jackal amrl))
)

(:metric minimize (total_distance_travelled))

)


