(define (domain jackal_world)
  (:types robot - object
          person - object
          deliverable - object
          location - object)
(:predicates (at ?x - object ?y - location)
             (has ?x - robot ?y - deliverable))

(:action pick-from
:parameters (?x - robot ?y - deliverable ?z - location)
:precondition (and (at ?x ?z)
                   (at ?y ?z)
                   (not (has ?x ?y)))
:effect (and (at ?x ?z)
             (not (at ?y ?z))
             (has ?x ?y)))

(:action drop-at
:parameters (?x - robot ?y - deliverable ?z - location)
:precondition (and (at ?x ?z)
                   (has ?x ?y))
:effect (and (at ?x ?z)
             (at ?y ?z)
             (not (has ?x ?y))))

(:action go-to
:parameters (?x - robot ?loc-from - location ?loc-to - location)
:precondition (and (not (at ?x ?loc-to))
                    (at ?x ?loc-from))
:effect (and (at ?x ?loc-to)
             (not (at ?x ?loc-from))))
)