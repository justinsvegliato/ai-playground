(define (problem simple_delivery)

(:domain world)

(:objects 
    jackal - robot
    package - deliverable
    roomA roomB roomC roomD - location)

(:init
    (at package roomA)
    (at jackal roomC)
    
    (= (distance roomA roomB) 10)
    (= (distance roomB roomA) 10)
    (= (distance roomB roomC) 22)
    (= (distance roomC roomB) 22)
    
    (connected roomA roomB)
    (connected roomB roomA)
    (connected roomB roomC)
    (connected roomC roomB)
    
    (= (total_distance_travelled) 0))

(:goal
    (at package roomC))

(:metric minimize (total_distance_travelled))

)


