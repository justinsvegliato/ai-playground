(define (problem complex_delivery)

(:domain world)

(:objects 
    jackal - robot
    package1 package2 - deliverable
    roomA roomB roomC roomD - location)

(:init
    (at package1 roomA)
    (at package2 roomB)
    (at jackal roomC)
    
    (= (distance roomA roomB) 10)
    (= (distance roomB roomA) 10)
    (= (distance roomB roomC) 10)
    (= (distance roomC roomB) 10)
    (= (distance roomC roomD) 10)
    (= (distance roomD roomC) 10)
    
    (connected roomA roomB)
    (connected roomB roomA)
    (connected roomB roomC)
    (connected roomC roomB)
    (connected roomC roomD)
    (connected roomD roomC)
    
    (= (total_distance_travelled) 0))

(:goal
    (and (at package1 roomD)
         (at package2 roomC)))

(:metric minimize (total_distance_travelled))

)


