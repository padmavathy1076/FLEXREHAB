"""
FLEXREHAB - Exercise Catalog & Visualization Keyframe Data
Provides comprehensive clinical exercise prescriptions and animation keyframe datasets
calibrated for Stroke Hemiparesis, Carpal Tunnel, and Tendon Repair Rehabilitation.
"""

from typing import Dict, List, Any, Optional

# Complete Exercise Catalog across Beginner, Intermediate, and Advanced therapy levels
EXERCISES_CATALOG: List[Dict[str, Any]] = [
    # -------------------------------------------------------------------------
    # BEGINNER (< 40% Recovery) - 9 Exercises: Range of Motion & Gentle Mobility
    # -------------------------------------------------------------------------
    {
        "id": "ex_001",
        "order": 1,
        "name": "Passive Finger Extension",
        "category": "Range of Motion",
        "therapy_level": "Beginner",
        "recovery_min": 0.0,
        "recovery_max": 40.0,
        "description": "Gently extend all five fingers upwards and backward to stretch the flexor tendons, counteract flexor spasticity, and open the palm.",
        "benefits": [
            "Relieves flexor tendon spasticity after prolonged curling",
            "Restores open-palm span necessary for stabilizing objects",
            "Promotes extensor digitorum communis tendon gliding"
        ],
        "instructions": [
            "Rest forearm comfortably on a flat surface with palm facing up.",
            "Slowly uncurl all fingers from the base knuckles upward.",
            "Gently extend all fingers until fully open and flat.",
            "Hold the extended open position for 5 seconds before gently relaxing."
        ],
        "duration": "5 mins",
        "duration_min": 5,
        "repetitions": "10 reps",
        "sets": "2 sets",
        "difficulty": "Easy",
        "target_fingers": ["Thumb", "Index", "Middle", "Ring", "Pinky"],
        "icon": "fa-solid fa-hand"
    },
    {
        "id": "ex_002",
        "order": 2,
        "name": "Gentle Fist Clench",
        "category": "Flexion Mobility",
        "therapy_level": "Beginner",
        "recovery_min": 0.0,
        "recovery_max": 40.0,
        "description": "Controlled, gentle curling of all fingers into a soft, relaxed fist followed by a smooth unfolding.",
        "benefits": [
            "Initiates deep digital flexor muscle activation without joint strain",
            "Maintains synovial fluid circulation in PIP and DIP joints",
            "Re-establishes neuromuscular feedback for cylindrical grasp"
        ],
        "instructions": [
            "Begin with hand open and fingers upright in a neutral posture.",
            "Slowly curl the fingertips inward toward the upper palm.",
            "Form a comfortable, relaxed fist without squeezing tightly.",
            "Hold for 3 seconds, then slowly unfurl fingers back to open."
        ],
        "duration": "5 mins",
        "duration_min": 5,
        "repetitions": "10 reps",
        "sets": "3 sets",
        "difficulty": "Easy",
        "target_fingers": ["Thumb", "Index", "Middle", "Ring", "Pinky"],
        "icon": "fa-solid fa-hand-back-fist"
    },
    {
        "id": "ex_003",
        "order": 3,
        "name": "Table Top Finger Lift",
        "category": "Extensor Activation",
        "therapy_level": "Beginner",
        "recovery_min": 0.0,
        "recovery_max": 40.0,
        "description": "Rest palm flat on a table and lift individual fingers upward one by one to practice neuromuscular fractionation.",
        "benefits": [
            "Fosters isolated extensor control without co-contracting neighbors",
            "Strengthens the extensor indicis and extensor digiti minimi",
            "Improves finger independence for typing and utensil handling"
        ],
        "instructions": [
            "Place palm completely flat on a table with fingers spread comfortably.",
            "Keep thumb, middle, and ring fingers flat while lifting index upward.",
            "Lower smoothly, then lift middle finger, followed by ring and pinky.",
            "Maintain steady, rhythmic lifting without tilting the wrist."
        ],
        "duration": "6 mins",
        "duration_min": 6,
        "repetitions": "8 reps each",
        "sets": "2 sets",
        "difficulty": "Easy",
        "target_fingers": ["Index", "Middle", "Ring", "Pinky"],
        "icon": "fa-solid fa-hand-point-up"
    },
    {
        "id": "ex_004",
        "order": 4,
        "name": "Thumb Abduction & Stretch",
        "category": "Thumb Mobility",
        "therapy_level": "Beginner",
        "recovery_min": 0.0,
        "recovery_max": 40.0,
        "description": "Move the thumb laterally away from the palm into an L-shape to stretch the first web space.",
        "benefits": [
            "Prevents adductor pollicis contracture and thumb webbing tightness",
            "Essential for grasping wide objects like cups and bottles",
            "Strengthens abductor pollicis brevis and longus"
        ],
        "instructions": [
            "Start with hand upright and thumb resting against the index finger.",
            "Move thumb directly outward away from the palm into an L-shape.",
            "Hold the extended abduction stretch for 4 seconds.",
            "Slowly bring the thumb back beside the index finger."
        ],
        "duration": "4 mins",
        "duration_min": 4,
        "repetitions": "12 reps",
        "sets": "3 sets",
        "difficulty": "Easy",
        "target_fingers": ["Thumb"],
        "icon": "fa-solid fa-thumbs-up"
    },
    {
        "id": "ex_005",
        "order": 5,
        "name": "Finger Spread & Squeeze",
        "category": "Interosseous Activation",
        "therapy_level": "Beginner",
        "recovery_min": 0.0,
        "recovery_max": 40.0,
        "description": "Spread all fingers as wide as possible into a fan, hold, and squeeze them tightly together.",
        "benefits": [
            "Activates dorsal interossei (abduction) and palmar interossei (adduction)",
            "Enhances lateral digital joint stability and grip breadth",
            "Reduces swelling and lymph accumulation in finger web spaces"
        ],
        "instructions": [
            "Hold hand upright with fingers straight and aligned.",
            "Fan out all five fingers as wide as comfortable.",
            "Hold the wide spread for 3 seconds.",
            "Bring all fingers firmly together side-by-side and squeeze gently."
        ],
        "duration": "5 mins",
        "duration_min": 5,
        "repetitions": "10 reps",
        "sets": "2 sets",
        "difficulty": "Easy",
        "target_fingers": ["Thumb", "Index", "Middle", "Ring", "Pinky"],
        "icon": "fa-solid fa-arrows-left-right"
    },
    {
        "id": "ex_006",
        "order": 6,
        "name": "Hook Fist Stretch",
        "category": "Tendon Gliding",
        "therapy_level": "Beginner",
        "recovery_min": 0.0,
        "recovery_max": 40.0,
        "description": "Bend only the PIP and DIP joints while keeping the MCP (knuckle) joints extended straight.",
        "benefits": [
            "Maximizes differential tendon excursion between FDS and FDP",
            "Prevents adhesion formation along the flexor tendon sheath",
            "Increases joint space in the distal interphalangeal joints"
        ],
        "instructions": [
            "Hold hand straight with fingers pointing upward.",
            "Bend only the top two joints of the four fingers downward into a hook.",
            "Keep the main knuckle joints completely straight and upright.",
            "Hold the hook shape for 4 seconds, then straighten."
        ],
        "duration": "5 mins",
        "duration_min": 5,
        "repetitions": "10 reps",
        "sets": "3 sets",
        "difficulty": "Medium",
        "target_fingers": ["Index", "Middle", "Ring", "Pinky"],
        "icon": "fa-solid fa-anchor"
    },
    {
        "id": "ex_007",
        "order": 7,
        "name": "Straight Fist Flexion",
        "category": "Tendon Gliding",
        "therapy_level": "Beginner",
        "recovery_min": 0.0,
        "recovery_max": 40.0,
        "description": "Bend MCP and PIP joints at 90 degrees while keeping DIP joints straight against the palm.",
        "benefits": [
            "Maximizes FDS tendon excursion relative to the bone surface",
            "Builds lumbrical muscle strength in 90-degree flexion",
            "Prepares hand for hook grasp and carrying handle bags"
        ],
        "instructions": [
            "Start with fingers straight and upright.",
            "Bend main knuckles and middle knuckles at 90 degrees.",
            "Keep the fingertip joints straight, pressing pads to the palm.",
            "Hold this flat-top position for 3 seconds, then release."
        ],
        "duration": "5 mins",
        "duration_min": 5,
        "repetitions": "10 reps",
        "sets": "2 sets",
        "difficulty": "Medium",
        "target_fingers": ["Index", "Middle", "Ring", "Pinky"],
        "icon": "fa-solid fa-square"
    },
    {
        "id": "ex_008",
        "order": 8,
        "name": "Wrist Flexion & Extension",
        "category": "Wrist Mobilization",
        "therapy_level": "Beginner",
        "recovery_min": 0.0,
        "recovery_max": 40.0,
        "description": "Slow, controlled bending of the wrist upward toward extension, then gently downward into flexion.",
        "benefits": [
            "Mobilizes the radiocarpal and midcarpal joint capsules",
            "Reduces median nerve compression in the carpal canal",
            "Restores the tenodesis effect essential for natural functional grasp"
        ],
        "instructions": [
            "Rest forearm on a table edge with hand dangling freely over the rim.",
            "Slowly lift the hand upward at the wrist joint as high as comfortable.",
            "Hold for 3 seconds, then lower down smoothly toward the floor.",
            "Keep fingers lightly relaxed and forearm resting flat."
        ],
        "duration": "4 mins",
        "duration_min": 4,
        "repetitions": "12 reps",
        "sets": "2 sets",
        "difficulty": "Easy",
        "target_fingers": ["Thumb", "Index", "Middle", "Ring", "Pinky"],
        "icon": "fa-solid fa-arrows-up-down"
    },
    {
        "id": "ex_009",
        "order": 9,
        "name": "Passive Assistive Stretch",
        "category": "Range of Motion",
        "therapy_level": "Beginner",
        "recovery_min": 0.0,
        "recovery_max": 40.0,
        "description": "Using gentle pressure, stretch the affected hand into full extension to reduce joint stiffness.",
        "benefits": [
            "Relieves morning stiffness and flexor contractures",
            "Realigns collagen fibers in recovering connective tissue",
            "Promotes relaxation through sustained end-range hold"
        ],
        "instructions": [
            "Place affected hand palm-up on a soft table or pillow.",
            "Gently apply steady backward pressure against the fingers.",
            "Hold stretch for 10 seconds without forcing past pain threshold.",
            "Release smoothly and repeat across all digits."
        ],
        "duration": "6 mins",
        "duration_min": 6,
        "repetitions": "5 reps",
        "sets": "2 sets",
        "difficulty": "Easy",
        "target_fingers": ["Thumb", "Index", "Middle", "Ring", "Pinky"],
        "icon": "fa-solid fa-hands-holding"
    },

    # -------------------------------------------------------------------------
    # INTERMEDIATE (40% - 70% Recovery) - 5 Exercises: Strength & Coordination
    # -------------------------------------------------------------------------
    {
        "id": "ex_010",
        "order": 1,
        "name": "Full Active Fist Clench",
        "category": "Strength & Power Grip",
        "therapy_level": "Intermediate",
        "recovery_min": 40.0,
        "recovery_max": 70.0,
        "description": "Forceful active clenching of all fingers into a tight fist with thumb wrapped securely, holding sustained isometric tension.",
        "benefits": [
            "Builds peak isometric grip strength for holding heavy objects",
            "Recruits both fast and slow-twitch digital flexor motor units",
            "Stabilizes wrist extensors during high-force grasping"
        ],
        "instructions": [
            "Open hand wide with fingers separated.",
            "Flex all fingers deeply into the palm.",
            "Wrap thumb firmly across the proximal index and middle fingers.",
            "Squeeze firmly for 5 seconds, then open wide and stretch."
        ],
        "duration": "6 mins",
        "duration_min": 6,
        "repetitions": "12 reps",
        "sets": "3 sets",
        "difficulty": "Medium",
        "target_fingers": ["Thumb", "Index", "Middle", "Ring", "Pinky"],
        "icon": "fa-solid fa-hand-fist"
    },
    {
        "id": "ex_011",
        "order": 2,
        "name": "Finger Tapping Sequence",
        "category": "Motor Coordination",
        "therapy_level": "Intermediate",
        "recovery_min": 40.0,
        "recovery_max": 70.0,
        "description": "Sequential rapid tapping of index, middle, ring, and pinky fingers in rhythm against a firm surface.",
        "benefits": [
            "Refines corticospinal tract timing and selective finger individuation",
            "Improves rhythmic sensorimotor coordination and agility",
            "Reduces synergistic cross-finger spastic coupling"
        ],
        "instructions": [
            "Rest hand palm-down flat on table.",
            "Tap index finger down firmly twice in succession.",
            "Tap middle finger twice, then ring finger, and finally pinky.",
            "Reverse direction and tap from pinky back to index smoothly."
        ],
        "duration": "5 mins",
        "duration_min": 5,
        "repetitions": "15 cycles",
        "sets": "3 sets",
        "difficulty": "Medium",
        "target_fingers": ["Index", "Middle", "Ring", "Pinky"],
        "icon": "fa-solid fa-music"
    },
    {
        "id": "ex_012",
        "order": 3,
        "name": "Claw Curl Stretch",
        "category": "Intrinsic Muscle Strength",
        "therapy_level": "Intermediate",
        "recovery_min": 40.0,
        "recovery_max": 70.0,
        "description": "High-intensity isometric claw curl flexing PIP and DIP joints while holding MCP knuckles firmly extended.",
        "benefits": [
            "Strengthens lumbricals and interossei muscles under high load",
            "Prevents metacarpophalangeal hyperextension deformities",
            "Develops muscular endurance for sustained gripping"
        ],
        "instructions": [
            "Hold hand upright in a vertical stop-sign position.",
            "Pull fingertips down tightly toward the base pads of the fingers.",
            "Keep wrist aligned and knuckles elevated.",
            "Hold the active claw squeeze for 5 seconds before releasing."
        ],
        "duration": "5 mins",
        "duration_min": 5,
        "repetitions": "10 reps",
        "sets": "3 sets",
        "difficulty": "Medium",
        "target_fingers": ["Index", "Middle", "Ring", "Pinky"],
        "icon": "fa-solid fa-cat"
    },
    {
        "id": "ex_013",
        "order": 4,
        "name": "Thumb-to-Fingertip Opposition",
        "category": "Fine Coordination",
        "therapy_level": "Intermediate",
        "recovery_min": 40.0,
        "recovery_max": 70.0,
        "description": "Touch the thumb pad sequentially to index, middle, ring, and little fingertips, creating a rounded 'O' ring shape.",
        "benefits": [
            "Restores thenar muscle opposition essential for daily living tasks",
            "Enhances tactile fingertip sensation and pad-to-pad grip",
            "Facilitates pen handling, eating with utensils, and buttoning"
        ],
        "instructions": [
            "Hold hand up with palm facing your face.",
            "Bring thumb pad and index fingertip together to form an 'O'.",
            "Open slightly and touch thumb to middle fingertip.",
            "Continue to ring finger, and finally little finger, then reverse."
        ],
        "duration": "6 mins",
        "duration_min": 6,
        "repetitions": "10 cycles",
        "sets": "3 sets",
        "difficulty": "Medium",
        "target_fingers": ["Thumb", "Index", "Middle", "Ring", "Pinky"],
        "icon": "fa-solid fa-circle-notch"
    },
    {
        "id": "ex_014",
        "order": 5,
        "name": "Wrist Radial-Ulnar Deviation",
        "category": "Wrist Stability",
        "therapy_level": "Intermediate",
        "recovery_min": 40.0,
        "recovery_max": 70.0,
        "description": "Wave hand side-to-side laterally at the wrist joint while keeping the forearm stationary on the table.",
        "benefits": [
            "Strengthens flexor and extensor carpi radialis and ulnaris",
            "Critical for pouring liquids, turning doorknobs, and hammer grips",
            "Balances medial and lateral wrist ligamentous support"
        ],
        "instructions": [
            "Place forearm and palm flat down on a table.",
            "Pivot wrist smoothly toward the thumb side (radial deviation).",
            "Pause 1 second, then pivot smoothly toward the pinky side (ulnar deviation).",
            "Perform in a controlled windshield-wiper arc without lifting forearm."
        ],
        "duration": "5 mins",
        "duration_min": 5,
        "repetitions": "15 reps",
        "sets": "2 sets",
        "difficulty": "Medium",
        "target_fingers": ["Thumb", "Pinky"],
        "icon": "fa-solid fa-arrows-left-right-to-line"
    },

    # -------------------------------------------------------------------------
    # ADVANCED (> 70% Recovery) - 2 Exercises: Fine Motor Skills & Precision
    # -------------------------------------------------------------------------
    {
        "id": "ex_015",
        "order": 1,
        "name": "Precision Pinch & Release",
        "category": "Fine Motor Dexterity",
        "therapy_level": "Advanced",
        "recovery_min": 70.0,
        "recovery_max": 100.0,
        "description": "High-dexterity micro-pinching between thumb pad and index fingertip with fine force control and rapid release.",
        "benefits": [
            "Calibrates sensitive sensory afferents in fingertip pulps",
            "Fine-tunes first dorsal interosseus and adductor pollicis synergy",
            "Essential for handling coins, needles, keys, and zipper pulls"
        ],
        "instructions": [
            "Hold hand up with thumb and index finger hovering 1 inch apart.",
            "Snap thumb and index tips together with firm, crisp precision.",
            "Hold pinch for 2 seconds while modulating force.",
            "Quickly snap back to the open ready position."
        ],
        "duration": "5 mins",
        "duration_min": 5,
        "repetitions": "20 reps",
        "sets": "3 sets",
        "difficulty": "Hard",
        "target_fingers": ["Thumb", "Index"],
        "icon": "fa-solid fa-hand-holding-hand"
    },
    {
        "id": "ex_016",
        "order": 2,
        "name": "Fine Motor Piano Tap",
        "category": "High-Speed Articulation",
        "therapy_level": "Advanced",
        "recovery_min": 70.0,
        "recovery_max": 100.0,
        "description": "High-speed, independent rhythmic fingertip drumming simulating rapid piano key playing with elevated palm arch.",
        "benefits": [
            "Maximizes neural fractionation of individual digital motor control",
            "Improves rapid reciprocal inhibition between digital flexors and extensors",
            "Returns hand to elite vocational dexterity for typing and instruments"
        ],
        "instructions": [
            "Arch hand with knuckles elevated, fingertips resting lightly on table.",
            "Rapidly strike the surface in sequence: Thumb, Index, Middle, Ring, Pinky.",
            "Maintain crisp individual finger strikes without neighbor fingers lifting.",
            "Increase tempo gradually while maintaining distinct keystroke rhythm."
        ],
        "duration": "6 mins",
        "duration_min": 6,
        "repetitions": "25 rapid cycles",
        "sets": "3 sets",
        "difficulty": "Hard",
        "target_fingers": ["Thumb", "Index", "Middle", "Ring", "Pinky"],
        "icon": "fa-solid fa-keyboard"
    }
]

# Map of Exercise ID to Keyframe Sequences
VISUALIZATION_KEYFRAMES: Dict[str, List[Dict[str, Any]]] = {
    # -------------------------------------------------------------------------
    # ex_001: Passive Finger Extension
    # -------------------------------------------------------------------------
    "ex_001": [
        {
            "step_number": 1,
            "step_total": 4,
            "title": "Resting Position",
            "description": "Rest forearm flat with fingers in a relaxed, comfortable curl.",
            "duration_ms": 1100,
            "fingers": {
                "thumb": {"angle": 30, "spread": 0},
                "index": {"angle": 35, "spread": 0},
                "middle": {"angle": 35, "spread": 0},
                "ring": {"angle": 35, "spread": 0},
                "pinky": {"angle": 35, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 2,
            "step_total": 4,
            "title": "Initiate Extension",
            "description": "Slowly begin opening all fingers outward from the knuckles.",
            "duration_ms": 1300,
            "fingers": {
                "thumb": {"angle": 15, "spread": -8},
                "index": {"angle": 15, "spread": -4},
                "middle": {"angle": 15, "spread": 0},
                "ring": {"angle": 15, "spread": 4},
                "pinky": {"angle": 15, "spread": 8}
            },
            "wrist": {"angle": -5, "rotation": 0}
        },
        {
            "step_number": 3,
            "step_total": 4,
            "title": "Full Extension Stretch",
            "description": "Gently stretch all fingers straight and open wide. Hold for 5 seconds.",
            "duration_ms": 1600,
            "fingers": {
                "thumb": {"angle": 0, "spread": -16},
                "index": {"angle": 0, "spread": -8},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 8},
                "pinky": {"angle": 0, "spread": 16}
            },
            "wrist": {"angle": -12, "rotation": 0}
        },
        {
            "step_number": 4,
            "step_total": 4,
            "title": "Smooth Relax",
            "description": "Gently relax fingers back to starting neutral posture.",
            "duration_ms": 1200,
            "fingers": {
                "thumb": {"angle": 25, "spread": 0},
                "index": {"angle": 28, "spread": 0},
                "middle": {"angle": 28, "spread": 0},
                "ring": {"angle": 28, "spread": 0},
                "pinky": {"angle": 28, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        }
    ],

    # -------------------------------------------------------------------------
    # ex_002: Gentle Fist Clench
    # -------------------------------------------------------------------------
    "ex_002": [
        {
            "step_number": 1,
            "step_total": 4,
            "title": "Open Starting Hand",
            "description": "Start with fingers fully open and pointing upright.",
            "duration_ms": 1100,
            "fingers": {
                "thumb": {"angle": 0, "spread": 0},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 2,
            "step_total": 4,
            "title": "Mid-Flexion Curl",
            "description": "Slowly curl fingertips toward the upper palm.",
            "duration_ms": 1300,
            "fingers": {
                "thumb": {"angle": 35, "spread": 5},
                "index": {"angle": 45, "spread": 2},
                "middle": {"angle": 45, "spread": 0},
                "ring": {"angle": 45, "spread": -2},
                "pinky": {"angle": 45, "spread": -4}
            },
            "wrist": {"angle": 5, "rotation": 0}
        },
        {
            "step_number": 3,
            "step_total": 4,
            "title": "Soft Closed Fist",
            "description": "Close all fingers gently into a relaxed fist without squeezing.",
            "duration_ms": 1600,
            "fingers": {
                "thumb": {"angle": 75, "spread": 12},
                "index": {"angle": 85, "spread": 0},
                "middle": {"angle": 85, "spread": 0},
                "ring": {"angle": 85, "spread": 0},
                "pinky": {"angle": 85, "spread": 0}
            },
            "wrist": {"angle": 8, "rotation": 0}
        },
        {
            "step_number": 4,
            "step_total": 4,
            "title": "Unfurl to Open",
            "description": "Smoothly unfold fingers back to full extension.",
            "duration_ms": 1200,
            "fingers": {
                "thumb": {"angle": 15, "spread": 0},
                "index": {"angle": 20, "spread": 0},
                "middle": {"angle": 20, "spread": 0},
                "ring": {"angle": 20, "spread": 0},
                "pinky": {"angle": 20, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        }
    ],

    # -------------------------------------------------------------------------
    # ex_003: Table Top Finger Lift
    # -------------------------------------------------------------------------
    "ex_003": [
        {
            "step_number": 1,
            "step_total": 5,
            "title": "Flat Rest",
            "description": "Place palm flat on table with all fingers straight.",
            "duration_ms": 1000,
            "fingers": {
                "thumb": {"angle": 0, "spread": 0},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 2,
            "step_total": 5,
            "title": "Index Finger Lift",
            "description": "Lift index finger upward off the surface while keeping others flat.",
            "duration_ms": 1300,
            "fingers": {
                "thumb": {"angle": 0, "spread": 0},
                "index": {"angle": -30, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 3,
            "step_total": 5,
            "title": "Middle Finger Lift",
            "description": "Lower index flat and isolate the middle finger upward.",
            "duration_ms": 1300,
            "fingers": {
                "thumb": {"angle": 0, "spread": 0},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": -32, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 4,
            "step_total": 5,
            "title": "Ring & Pinky Lift",
            "description": "Lift ring and little fingers upward together smoothly.",
            "duration_ms": 1300,
            "fingers": {
                "thumb": {"angle": 0, "spread": 0},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 28, "spread": 0},
                "pinky": {"angle": 30, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 5,
            "step_total": 5,
            "title": "Rest Flat",
            "description": "Lower all fingers back flat to surface.",
            "duration_ms": 1000,
            "fingers": {
                "thumb": {"angle": 0, "spread": 0},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        }
    ],

    # -------------------------------------------------------------------------
    # ex_004: Thumb Abduction & Stretch
    # -------------------------------------------------------------------------
    "ex_004": [
        {
            "step_number": 1,
            "step_total": 4,
            "title": "Adducted Start",
            "description": "Thumb rested alongside the index finger.",
            "duration_ms": 1000,
            "fingers": {
                "thumb": {"angle": 10, "spread": 5},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 2,
            "step_total": 4,
            "title": "Move Outward",
            "description": "Slowly extend thumb outward away from the palm.",
            "duration_ms": 1200,
            "fingers": {
                "thumb": {"angle": 0, "spread": -22},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 3,
            "step_total": 4,
            "title": "Hold L-Shape Stretch",
            "description": "Hold thumb in maximum abduction stretch for 4 seconds.",
            "duration_ms": 1600,
            "fingers": {
                "thumb": {"angle": -5, "spread": -42},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": -5}
        },
        {
            "step_number": 4,
            "step_total": 4,
            "title": "Return Together",
            "description": "Bring thumb smoothly back beside index finger.",
            "duration_ms": 1100,
            "fingers": {
                "thumb": {"angle": 8, "spread": 2},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        }
    ],

    # -------------------------------------------------------------------------
    # ex_005: Finger Spread & Squeeze
    # -------------------------------------------------------------------------
    "ex_005": [
        {
            "step_number": 1,
            "step_total": 4,
            "title": "Fingers Together",
            "description": "Keep fingers aligned side-by-side in neutral position.",
            "duration_ms": 1000,
            "fingers": {
                "thumb": {"angle": 0, "spread": 0},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 2,
            "step_total": 4,
            "title": "Begin Spreading",
            "description": "Spread all fingers outward like an opening hand fan.",
            "duration_ms": 1200,
            "fingers": {
                "thumb": {"angle": 0, "spread": -18},
                "index": {"angle": 0, "spread": -10},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 10},
                "pinky": {"angle": 0, "spread": 18}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 3,
            "step_total": 4,
            "title": "Maximum Fan Stretch",
            "description": "Hold fingers spread as wide apart as comfortable for 3 seconds.",
            "duration_ms": 1500,
            "fingers": {
                "thumb": {"angle": 0, "spread": -34},
                "index": {"angle": 0, "spread": -18},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 18},
                "pinky": {"angle": 0, "spread": 34}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 4,
            "step_total": 4,
            "title": "Squeeze Back Together",
            "description": "Bring all fingers firmly together side-by-side.",
            "duration_ms": 1100,
            "fingers": {
                "thumb": {"angle": 0, "spread": 0},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        }
    ],

    # -------------------------------------------------------------------------
    # ex_006: Hook Fist Stretch
    # -------------------------------------------------------------------------
    "ex_006": [
        {
            "step_number": 1,
            "step_total": 4,
            "title": "Straight Fingers",
            "description": "Hold hand straight with fingers pointing upright.",
            "duration_ms": 1000,
            "fingers": {
                "thumb": {"angle": 0, "spread": 0},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 2,
            "step_total": 4,
            "title": "Bend Top Knuckles",
            "description": "Bend only the top two joints while holding big knuckles straight.",
            "duration_ms": 1200,
            "fingers": {
                "thumb": {"angle": 15, "spread": 0},
                "index": {"angle": 45, "spread": 0},
                "middle": {"angle": 45, "spread": 0},
                "ring": {"angle": 45, "spread": 0},
                "pinky": {"angle": 45, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 3,
            "step_total": 4,
            "title": "Full Hook Fist",
            "description": "Maintain deep hook posture for 4 seconds.",
            "duration_ms": 1600,
            "fingers": {
                "thumb": {"angle": 25, "spread": 0},
                "index": {"angle": 80, "spread": 0},
                "middle": {"angle": 80, "spread": 0},
                "ring": {"angle": 80, "spread": 0},
                "pinky": {"angle": 80, "spread": 0}
            },
            "wrist": {"angle": 5, "rotation": 0}
        },
        {
            "step_number": 4,
            "step_total": 4,
            "title": "Straighten Back",
            "description": "Unfurl back to completely straight fingers.",
            "duration_ms": 1100,
            "fingers": {
                "thumb": {"angle": 0, "spread": 0},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        }
    ],

    # -------------------------------------------------------------------------
    # ex_007: Straight Fist Flexion
    # -------------------------------------------------------------------------
    "ex_007": [
        {
            "step_number": 1,
            "step_total": 4,
            "title": "Starting Open",
            "description": "Hand upright with all fingers straight.",
            "duration_ms": 1000,
            "fingers": {
                "thumb": {"angle": 0, "spread": 0},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 2,
            "step_total": 4,
            "title": "Bend Knuckles 90°",
            "description": "Bend knuckles at 90° while keeping fingertip pads straight.",
            "duration_ms": 1300,
            "fingers": {
                "thumb": {"angle": 20, "spread": 0},
                "index": {"angle": 48, "spread": 0},
                "middle": {"angle": 48, "spread": 0},
                "ring": {"angle": 48, "spread": 0},
                "pinky": {"angle": 48, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 3,
            "step_total": 4,
            "title": "Straight Fist Peak",
            "description": "Hold flat tabletop fist with fingertips touching palm.",
            "duration_ms": 1500,
            "fingers": {
                "thumb": {"angle": 35, "spread": 0},
                "index": {"angle": 75, "spread": 0},
                "middle": {"angle": 75, "spread": 0},
                "ring": {"angle": 75, "spread": 0},
                "pinky": {"angle": 75, "spread": 0}
            },
            "wrist": {"angle": 5, "rotation": 0}
        },
        {
            "step_number": 4,
            "step_total": 4,
            "title": "Open Return",
            "description": "Smoothly unfold fingers back to open hand.",
            "duration_ms": 1100,
            "fingers": {
                "thumb": {"angle": 0, "spread": 0},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        }
    ],

    # -------------------------------------------------------------------------
    # ex_008: Wrist Flexion & Extension
    # -------------------------------------------------------------------------
    "ex_008": [
        {
            "step_number": 1,
            "step_total": 4,
            "title": "Neutral Alignment",
            "description": "Forearm rested flat with wrist in neutral alignment.",
            "duration_ms": 1000,
            "fingers": {
                "thumb": {"angle": 10, "spread": 0},
                "index": {"angle": 10, "spread": 0},
                "middle": {"angle": 10, "spread": 0},
                "ring": {"angle": 10, "spread": 0},
                "pinky": {"angle": 10, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 2,
            "step_total": 4,
            "title": "Wrist Extension Upward",
            "description": "Slowly extend hand upward at the wrist joint.",
            "duration_ms": 1400,
            "fingers": {
                "thumb": {"angle": 0, "spread": 0},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": -35, "rotation": 0}
        },
        {
            "step_number": 3,
            "step_total": 4,
            "title": "Pass Through Neutral",
            "description": "Smooth transition back through neutral center.",
            "duration_ms": 1000,
            "fingers": {
                "thumb": {"angle": 10, "spread": 0},
                "index": {"angle": 10, "spread": 0},
                "middle": {"angle": 10, "spread": 0},
                "ring": {"angle": 10, "spread": 0},
                "pinky": {"angle": 10, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 4,
            "step_total": 4,
            "title": "Wrist Flexion Downward",
            "description": "Flex hand downward toward the floor stretching wrist extensors.",
            "duration_ms": 1400,
            "fingers": {
                "thumb": {"angle": 25, "spread": 0},
                "index": {"angle": 25, "spread": 0},
                "middle": {"angle": 25, "spread": 0},
                "ring": {"angle": 25, "spread": 0},
                "pinky": {"angle": 25, "spread": 0}
            },
            "wrist": {"angle": 35, "rotation": 0}
        }
    ],

    # -------------------------------------------------------------------------
    # ex_009: Passive Assistive Stretch
    # -------------------------------------------------------------------------
    "ex_009": [
        {
            "step_number": 1,
            "step_total": 4,
            "title": "Relaxed Posture",
            "description": "Affected hand placed palm-up in natural rest.",
            "duration_ms": 1000,
            "fingers": {
                "thumb": {"angle": 25, "spread": 0},
                "index": {"angle": 30, "spread": 0},
                "middle": {"angle": 30, "spread": 0},
                "ring": {"angle": 30, "spread": 0},
                "pinky": {"angle": 30, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 2,
            "step_total": 4,
            "title": "Gentle Extension Assist",
            "description": "Gently press fingers backward using the opposite hand.",
            "duration_ms": 1300,
            "fingers": {
                "thumb": {"angle": 10, "spread": -5},
                "index": {"angle": 8, "spread": -3},
                "middle": {"angle": 8, "spread": 0},
                "ring": {"angle": 8, "spread": 3},
                "pinky": {"angle": 8, "spread": 5}
            },
            "wrist": {"angle": -8, "rotation": 0}
        },
        {
            "step_number": 3,
            "step_total": 4,
            "title": "Full Passive Stretch",
            "description": "Hold gentle full palm extension stretch for 10 seconds.",
            "duration_ms": 1600,
            "fingers": {
                "thumb": {"angle": -8, "spread": -15},
                "index": {"angle": -10, "spread": -8},
                "middle": {"angle": -10, "spread": 0},
                "ring": {"angle": 10, "spread": 8},
                "pinky": {"angle": 10, "spread": 15}
            },
            "wrist": {"angle": -18, "rotation": 0}
        },
        {
            "step_number": 4,
            "step_total": 4,
            "title": "Release Gently",
            "description": "Slowly ease pressure and allow fingers to relax.",
            "duration_ms": 1100,
            "fingers": {
                "thumb": {"angle": 20, "spread": 0},
                "index": {"angle": 25, "spread": 0},
                "middle": {"angle": 25, "spread": 0},
                "ring": {"angle": 25, "spread": 0},
                "pinky": {"angle": 25, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        }
    ],

    # -------------------------------------------------------------------------
    # ex_010: Full Active Fist Clench
    # -------------------------------------------------------------------------
    "ex_010": [
        {
            "step_number": 1,
            "step_total": 4,
            "title": "Open Wide Spread",
            "description": "Open hand wide with fingers splayed and energized.",
            "duration_ms": 1000,
            "fingers": {
                "thumb": {"angle": 0, "spread": -16},
                "index": {"angle": 0, "spread": -8},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 8},
                "pinky": {"angle": 0, "spread": 16}
            },
            "wrist": {"angle": -8, "rotation": 0}
        },
        {
            "step_number": 2,
            "step_total": 4,
            "title": "Rapid Flexion Closure",
            "description": "Powerfully curl fingers into palm.",
            "duration_ms": 1200,
            "fingers": {
                "thumb": {"angle": 45, "spread": 8},
                "index": {"angle": 55, "spread": 0},
                "middle": {"angle": 55, "spread": 0},
                "ring": {"angle": 55, "spread": 0},
                "pinky": {"angle": 55, "spread": 0}
            },
            "wrist": {"angle": 5, "rotation": 0}
        },
        {
            "step_number": 3,
            "step_total": 4,
            "title": "Max Isometric Power Squeeze",
            "description": "Wrap thumb tightly and squeeze maximum firm fist for 5 seconds.",
            "duration_ms": 1700,
            "fingers": {
                "thumb": {"angle": 85, "spread": 18},
                "index": {"angle": 90, "spread": 0},
                "middle": {"angle": 90, "spread": 0},
                "ring": {"angle": 90, "spread": 0},
                "pinky": {"angle": 90, "spread": 0}
            },
            "wrist": {"angle": 12, "rotation": 0}
        },
        {
            "step_number": 4,
            "step_total": 4,
            "title": "Explosive Release to Open",
            "description": "Release fist and spring back open wide.",
            "duration_ms": 1100,
            "fingers": {
                "thumb": {"angle": 0, "spread": -14},
                "index": {"angle": 0, "spread": -6},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 6},
                "pinky": {"angle": 0, "spread": 14}
            },
            "wrist": {"angle": -5, "rotation": 0}
        }
    ],

    # -------------------------------------------------------------------------
    # ex_011: Finger Tapping Sequence
    # -------------------------------------------------------------------------
    "ex_011": [
        {
            "step_number": 1,
            "step_total": 5,
            "title": "Ready Posture",
            "description": "Rest all fingers lightly curved above the surface.",
            "duration_ms": 900,
            "fingers": {
                "thumb": {"angle": 15, "spread": 0},
                "index": {"angle": 15, "spread": 0},
                "middle": {"angle": 15, "spread": 0},
                "ring": {"angle": 15, "spread": 0},
                "pinky": {"angle": 15, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 2,
            "step_total": 5,
            "title": "Index Finger Tap",
            "description": "Tap index finger down firmly twice.",
            "duration_ms": 1100,
            "fingers": {
                "thumb": {"angle": 15, "spread": 0},
                "index": {"angle": 55, "spread": 0},
                "middle": {"angle": 10, "spread": 0},
                "ring": {"angle": 10, "spread": 0},
                "pinky": {"angle": 10, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 3,
            "step_total": 5,
            "title": "Middle Finger Tap",
            "description": "Tap middle finger down with crisp rhythmic control.",
            "duration_ms": 1100,
            "fingers": {
                "thumb": {"angle": 15, "spread": 0},
                "index": {"angle": 10, "spread": 0},
                "middle": {"angle": 55, "spread": 0},
                "ring": {"angle": 10, "spread": 0},
                "pinky": {"angle": 10, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 4,
            "step_total": 5,
            "title": "Ring Finger Tap",
            "description": "Tap ring finger independently without pinky moving.",
            "duration_ms": 1100,
            "fingers": {
                "thumb": {"angle": 15, "spread": 0},
                "index": {"angle": 10, "spread": 0},
                "middle": {"angle": 10, "spread": 0},
                "ring": {"angle": 55, "spread": 0},
                "pinky": {"angle": 10, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 5,
            "step_total": 5,
            "title": "Pinky Finger Tap",
            "description": "Tap pinky finger down sharply to complete the cycle.",
            "duration_ms": 1100,
            "fingers": {
                "thumb": {"angle": 15, "spread": 0},
                "index": {"angle": 10, "spread": 0},
                "middle": {"angle": 10, "spread": 0},
                "ring": {"angle": 10, "spread": 0},
                "pinky": {"angle": 55, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        }
    ],

    # -------------------------------------------------------------------------
    # ex_012: Claw Curl Stretch
    # -------------------------------------------------------------------------
    "ex_012": [
        {
            "step_number": 1,
            "step_total": 4,
            "title": "Flat Hand Posture",
            "description": "Hand straight up in a stop-sign position.",
            "duration_ms": 1000,
            "fingers": {
                "thumb": {"angle": 0, "spread": 0},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 2,
            "step_total": 4,
            "title": "Initiate Claw Squeeze",
            "description": "Draw fingertips downward toward the palm pads.",
            "duration_ms": 1200,
            "fingers": {
                "thumb": {"angle": 25, "spread": 0},
                "index": {"angle": 50, "spread": 0},
                "middle": {"angle": 50, "spread": 0},
                "ring": {"angle": 50, "spread": 0},
                "pinky": {"angle": 50, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 3,
            "step_total": 4,
            "title": "Deep Claw Hold",
            "description": "Squeeze deep claw shape with knuckles upright for 5 seconds.",
            "duration_ms": 1600,
            "fingers": {
                "thumb": {"angle": 40, "spread": 0},
                "index": {"angle": 88, "spread": 0},
                "middle": {"angle": 88, "spread": 0},
                "ring": {"angle": 88, "spread": 0},
                "pinky": {"angle": 88, "spread": 0}
            },
            "wrist": {"angle": -5, "rotation": 0}
        },
        {
            "step_number": 4,
            "step_total": 4,
            "title": "Snap Open",
            "description": "Quickly straighten all fingers back to open hand.",
            "duration_ms": 1100,
            "fingers": {
                "thumb": {"angle": 0, "spread": 0},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        }
    ],

    # -------------------------------------------------------------------------
    # ex_013: Thumb-to-Fingertip Opposition
    # -------------------------------------------------------------------------
    "ex_013": [
        {
            "step_number": 1,
            "step_total": 5,
            "title": "Thumb to Index 'O'",
            "description": "Pinch thumb and index tips together to form a round 'O' ring.",
            "duration_ms": 1300,
            "fingers": {
                "thumb": {"angle": 55, "spread": 10},
                "index": {"angle": 60, "spread": 0},
                "middle": {"angle": 10, "spread": 0},
                "ring": {"angle": 10, "spread": 0},
                "pinky": {"angle": 10, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 2,
            "step_total": 5,
            "title": "Thumb to Middle 'O'",
            "description": "Open slightly and pinch thumb to middle fingertip.",
            "duration_ms": 1300,
            "fingers": {
                "thumb": {"angle": 62, "spread": 12},
                "index": {"angle": 10, "spread": 0},
                "middle": {"angle": 65, "spread": 0},
                "ring": {"angle": 10, "spread": 0},
                "pinky": {"angle": 10, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 3,
            "step_total": 5,
            "title": "Thumb to Ring 'O'",
            "description": "Touch thumb to ring fingertip with firm pad contact.",
            "duration_ms": 1300,
            "fingers": {
                "thumb": {"angle": 68, "spread": 15},
                "index": {"angle": 10, "spread": 0},
                "middle": {"angle": 10, "spread": 0},
                "ring": {"angle": 68, "spread": 0},
                "pinky": {"angle": 10, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 4,
            "step_total": 5,
            "title": "Thumb to Pinky Opposition",
            "description": "Touch thumb to little fingertip across the entire palm.",
            "duration_ms": 1400,
            "fingers": {
                "thumb": {"angle": 75, "spread": 20},
                "index": {"angle": 10, "spread": 0},
                "middle": {"angle": 10, "spread": 0},
                "ring": {"angle": 10, "spread": 0},
                "pinky": {"angle": 75, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 5}
        },
        {
            "step_number": 5,
            "step_total": 5,
            "title": "Open Stretch",
            "description": "Open hand wide and stretch thumb outward.",
            "duration_ms": 1000,
            "fingers": {
                "thumb": {"angle": 0, "spread": -15},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        }
    ],

    # -------------------------------------------------------------------------
    # ex_014: Wrist Radial-Ulnar Deviation
    # -------------------------------------------------------------------------
    "ex_014": [
        {
            "step_number": 1,
            "step_total": 4,
            "title": "Center Alignment",
            "description": "Hand aligned straight in line with forearm.",
            "duration_ms": 1000,
            "fingers": {
                "thumb": {"angle": 5, "spread": 0},
                "index": {"angle": 5, "spread": 0},
                "middle": {"angle": 5, "spread": 0},
                "ring": {"angle": 5, "spread": 0},
                "pinky": {"angle": 5, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 2,
            "step_total": 4,
            "title": "Radial Deviation (Thumb Side)",
            "description": "Pivot wrist laterally toward the thumb side.",
            "duration_ms": 1300,
            "fingers": {
                "thumb": {"angle": 0, "spread": -5},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": -26}
        },
        {
            "step_number": 3,
            "step_total": 4,
            "title": "Center Transition",
            "description": "Smooth transition back through neutral center.",
            "duration_ms": 900,
            "fingers": {
                "thumb": {"angle": 5, "spread": 0},
                "index": {"angle": 5, "spread": 0},
                "middle": {"angle": 5, "spread": 0},
                "ring": {"angle": 5, "spread": 0},
                "pinky": {"angle": 5, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 4,
            "step_total": 4,
            "title": "Ulnar Deviation (Pinky Side)",
            "description": "Pivot wrist laterally toward the pinky side.",
            "duration_ms": 1300,
            "fingers": {
                "thumb": {"angle": 0, "spread": 0},
                "index": {"angle": 0, "spread": 0},
                "middle": {"angle": 0, "spread": 0},
                "ring": {"angle": 0, "spread": 0},
                "pinky": {"angle": 0, "spread": 5}
            },
            "wrist": {"angle": 0, "rotation": 28}
        }
    ],

    # -------------------------------------------------------------------------
    # ex_015: Precision Pinch & Release
    # -------------------------------------------------------------------------
    "ex_015": [
        {
            "step_number": 1,
            "step_total": 4,
            "title": "Pinch Ready Position",
            "description": "Thumb and index finger hovering 1 inch apart in precision alignment.",
            "duration_ms": 1000,
            "fingers": {
                "thumb": {"angle": 25, "spread": 5},
                "index": {"angle": 25, "spread": 0},
                "middle": {"angle": 35, "spread": 0},
                "ring": {"angle": 45, "spread": 0},
                "pinky": {"angle": 50, "spread": 0}
            },
            "wrist": {"angle": -5, "rotation": 0}
        },
        {
            "step_number": 2,
            "step_total": 4,
            "title": "Crisp Tip Pinch Contact",
            "description": "Snap thumb and index tips together with firm, precise pressure.",
            "duration_ms": 1200,
            "fingers": {
                "thumb": {"angle": 65, "spread": 12},
                "index": {"angle": 65, "spread": 0},
                "middle": {"angle": 35, "spread": 0},
                "ring": {"angle": 45, "spread": 0},
                "pinky": {"angle": 50, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 3,
            "step_total": 4,
            "title": "Sustain Fine Pinch Pressure",
            "description": "Hold precision pincer contact for 2 seconds.",
            "duration_ms": 1500,
            "fingers": {
                "thumb": {"angle": 68, "spread": 14},
                "index": {"angle": 68, "spread": 0},
                "middle": {"angle": 35, "spread": 0},
                "ring": {"angle": 45, "spread": 0},
                "pinky": {"angle": 50, "spread": 0}
            },
            "wrist": {"angle": 0, "rotation": 0}
        },
        {
            "step_number": 4,
            "step_total": 4,
            "title": "Quick Release to Hover",
            "description": "Snap quickly back to ready hover position.",
            "duration_ms": 1000,
            "fingers": {
                "thumb": {"angle": 20, "spread": 5},
                "index": {"angle": 20, "spread": 0},
                "middle": {"angle": 30, "spread": 0},
                "ring": {"angle": 40, "spread": 0},
                "pinky": {"angle": 45, "spread": 0}
            },
            "wrist": {"angle": -5, "rotation": 0}
        }
    ],

    # -------------------------------------------------------------------------
    # ex_016: Fine Motor Piano Tap
    # -------------------------------------------------------------------------
    "ex_016": [
        {
            "step_number": 1,
            "step_total": 6,
            "title": "Arched Hand Ready",
            "description": "Elevate palm arch with fingertips resting lightly on surface.",
            "duration_ms": 800,
            "fingers": {
                "thumb": {"angle": 20, "spread": 0},
                "index": {"angle": 25, "spread": 0},
                "middle": {"angle": 25, "spread": 0},
                "ring": {"angle": 25, "spread": 0},
                "pinky": {"angle": 25, "spread": 0}
            },
            "wrist": {"angle": -8, "rotation": 0}
        },
        {
            "step_number": 2,
            "step_total": 6,
            "title": "Thumb Keystroke",
            "description": "Strike surface crisply with the thumb pad.",
            "duration_ms": 900,
            "fingers": {
                "thumb": {"angle": 55, "spread": 8},
                "index": {"angle": 20, "spread": 0},
                "middle": {"angle": 20, "spread": 0},
                "ring": {"angle": 20, "spread": 0},
                "pinky": {"angle": 20, "spread": 0}
            },
            "wrist": {"angle": -6, "rotation": 0}
        },
        {
            "step_number": 3,
            "step_total": 6,
            "title": "Index Keystroke",
            "description": "Strike surface crisply with index finger.",
            "duration_ms": 900,
            "fingers": {
                "thumb": {"angle": 20, "spread": 0},
                "index": {"angle": 60, "spread": 0},
                "middle": {"angle": 20, "spread": 0},
                "ring": {"angle": 20, "spread": 0},
                "pinky": {"angle": 20, "spread": 0}
            },
            "wrist": {"angle": -6, "rotation": 0}
        },
        {
            "step_number": 4,
            "step_total": 6,
            "title": "Middle Keystroke",
            "description": "Strike surface crisply with middle finger.",
            "duration_ms": 900,
            "fingers": {
                "thumb": {"angle": 20, "spread": 0},
                "index": {"angle": 20, "spread": 0},
                "middle": {"angle": 60, "spread": 0},
                "ring": {"angle": 20, "spread": 0},
                "pinky": {"angle": 20, "spread": 0}
            },
            "wrist": {"angle": -6, "rotation": 0}
        },
        {
            "step_number": 5,
            "step_total": 6,
            "title": "Ring Keystroke",
            "description": "Strike surface crisply with ring finger.",
            "duration_ms": 900,
            "fingers": {
                "thumb": {"angle": 20, "spread": 0},
                "index": {"angle": 20, "spread": 0},
                "middle": {"angle": 20, "spread": 0},
                "ring": {"angle": 60, "spread": 0},
                "pinky": {"angle": 20, "spread": 0}
            },
            "wrist": {"angle": -6, "rotation": 0}
        },
        {
            "step_number": 6,
            "step_total": 6,
            "title": "Pinky Keystroke",
            "description": "Strike surface crisply with pinky finger to complete rapid run.",
            "duration_ms": 900,
            "fingers": {
                "thumb": {"angle": 20, "spread": 0},
                "index": {"angle": 20, "spread": 0},
                "middle": {"angle": 20, "spread": 0},
                "ring": {"angle": 20, "spread": 0},
                "pinky": {"angle": 60, "spread": 0}
            },
            "wrist": {"angle": -6, "rotation": 0}
        }
    ]
}


def get_all_exercises() -> List[Dict[str, Any]]:
    """Return all exercises in the catalog."""
    return EXERCISES_CATALOG


def get_exercise_by_id(exercise_id: str) -> Optional[Dict[str, Any]]:
    """Lookup single exercise by ID."""
    for ex in EXERCISES_CATALOG:
        if ex["id"].lower() == exercise_id.lower():
            return ex
    return None


def get_exercises_by_level(therapy_level: str) -> List[Dict[str, Any]]:
    """
    Filter exercises by therapy level: Beginner, Intermediate, Advanced.
    Case-insensitive matching.
    """
    target = therapy_level.strip().capitalize()
    results = [ex for ex in EXERCISES_CATALOG if ex["therapy_level"].capitalize() == target]
    if not results:
        # Default fallback to Beginner if unknown level provided
        results = [ex for ex in EXERCISES_CATALOG if ex["therapy_level"] == "Beginner"]
    return results


def get_exercises_for_patient(patient_score: float, current_level: str = "Beginner") -> List[Dict[str, Any]]:
    """
    Determine appropriate exercise prescription based on patient's latest recovery score.
    - Beginner: < 40% (8-9 exercises)
    - Intermediate: 40% - 70% (5 exercises)
    - Advanced: > 70% (1-2 exercises)
    """
    if patient_score < 40.0:
        return get_exercises_by_level("Beginner")
    elif patient_score <= 70.0:
        return get_exercises_by_level("Intermediate")
    else:
        return get_exercises_by_level("Advanced")


def get_visualization_keyframes(exercise_id: str) -> List[Dict[str, Any]]:
    """
    Retrieve animation keyframes for the given exercise ID.
    If not found, returns fallback keyframes for ex_001.
    """
    clean_id = exercise_id.strip().lower()
    return VISUALIZATION_KEYFRAMES.get(clean_id, VISUALIZATION_KEYFRAMES.get("ex_001", []))


# ============================================================================
# EXPORTED COLLECTIONS FOR APP.PY
# ============================================================================
ALL_EXERCISES: List[Dict[str, Any]] = EXERCISES_CATALOG

EXERCISES_DICT: Dict[str, Dict[str, Any]] = {ex["id"]: ex for ex in EXERCISES_CATALOG}

EXERCISES_BY_LEVEL: Dict[str, List[Dict[str, Any]]] = {
    "Beginner": [ex for ex in EXERCISES_CATALOG if ex["therapy_level"] == "Beginner"],
    "Intermediate": [ex for ex in EXERCISES_CATALOG if ex["therapy_level"] == "Intermediate"],
    "Advanced": [ex for ex in EXERCISES_CATALOG if ex["therapy_level"] == "Advanced"],
}

# Rich visualization dictionary matching app.py api_get_visualization
VISUALIZATION_DATA: Dict[str, Dict[str, Any]] = {}
for _ex in EXERCISES_CATALOG:
    _eid = _ex["id"]
    _kframes = VISUALIZATION_KEYFRAMES.get(_eid, VISUALIZATION_KEYFRAMES["ex_001"])
    _total_dur = sum(f.get("duration_ms", 1200) for f in _kframes)
    VISUALIZATION_DATA[_eid] = {
        "id": _eid,
        "name": _ex["name"],
        "animation_type": _ex.get("category", "General").lower().replace(" ", "_"),
        "description": _ex["description"],
        "therapy_level": _ex["therapy_level"],
        "total_duration_ms": _total_dur,
        "keyframes": _kframes
    }

