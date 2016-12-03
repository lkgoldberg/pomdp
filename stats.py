'''
    Statistics needed for POMDP model
'''

# Sensitivity and specificity statistics for self-diagnosis
SDStats = {
    "sens": 0.44,
    "spec": 0.92
}

# Sensitivity and specificity statistics for Mammography
MStats = {
    # Age group 40-49
    0: {
        "sens": 0.722,
        "spec": 0.889
    },
    # Age group 50-54
    1: {
        "sens": 0.722,
        "spec": 0.893
    },
    # Age group 55-59
    2: {
        "sens": 0.81,
        "spec": 0.893
    },
    # Age group 60-69
    3: {
        "sens": 0.81,
        "spec": 0.897
    },
    # Age group 70+
    4: {
        "sens": 0.862,
        "spec": 0.897
    }
}