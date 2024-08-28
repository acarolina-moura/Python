def calculate_media (media):
    if media >= 60:
        print('You pass the course!')
    else: 
        print('You not pass the course!')

calculate_media(60)



def pass_course(score):
    if score >= 80:
        print('You pass the course with flying colors!')
    elif score >= 65:
        print('You pass the course! Talk to your instructor.')
    else:
        print('You do not pass the course!')

pass_course(80)