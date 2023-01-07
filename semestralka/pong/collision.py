import numpy as np



#to assure the game is never too slow
MAX_ANGLE = np.pi/5
#the ball gets faster each bounce
BOUNCE_INCREASE = 1.1


def front_paddle_intersect(ball, line_x, line_y, line_length):
    if abs(ball.pos_x - line_x) > ball.RADIUS:
        return False

    intersect1 = ball.pos_y + np.sqrt(ball.RADIUS**2 - (ball.pos_x - line_x)**2)
    intersect2 = ball.pos_y - np.sqrt(ball.RADIUS**2 - (ball.pos_x - line_x)**2)

    if line_y <= intersect1 <= line_y + line_length or line_y <= intersect2 <= line_y + line_length:
        return True
    return False


def top_paddle_intersect(ball, line_x, line_y, line_length):
    if abs(ball.pos_y - line_y) > ball.RADIUS:
        return False

    intersect1 = ball.pos_x + np.sqrt(ball.RADIUS**2 - (ball.pos_y - line_y)**2)
    intersect2 = ball.pos_x - np.sqrt(ball.RADIUS**2 - (ball.pos_y - line_y)**2)

    if line_x <= intersect1 <= line_x + line_length or line_x <= intersect2 <= line_x + line_length:
        return True
    return False


def deflection_angle(ball, paddle):
    ball_distance = paddle.pos_y + paddle.height/2 - ball.pos_y
    relative_distance = 2*ball_distance/paddle.height

    if -1 < relative_distance < 1:
        return MAX_ANGLE * relative_distance
    return MAX_ANGLE * np.sign(relative_distance)


def new_direction(ball, paddle):
    angle = deflection_angle(ball, paddle) + ball.angle() / 2
    velocity = np.clip(0, ball.RADIUS, ball.total_velocity() * BOUNCE_INCREASE)

    return (velocity * np.cos(angle), - velocity * np.sin(angle))


def corner_bounce(ball, paddle):
    direction = - np.sign(ball.x_velocity)
    angle = np.pi/4 * np.sign(paddle.pos_y + paddle.height/2 - ball.pos_y)
    velocity = np.clip(0, ball.RADIUS, ball.total_velocity() * BOUNCE_INCREASE)

    ball.x_velocity = velocity * np.cos(angle) * direction
    ball.y_velocity = - velocity * np.sin(angle)


def front_bounce(ball, paddle):
    direction = np.sign(ball.x_velocity)

    ball.x_velocity, ball.y_velocity = new_direction(ball, paddle)
    ball.x_velocity *= -direction


def top_bounce(ball):
    ball.y_velocity *= -1


def bounce(ball, paddle, front_intersect, top_intersect):
    if front_intersect and top_intersect and not (paddle.pos_y < ball.pos_y < paddle.pos_y + paddle.height):
        corner_bounce(ball, paddle)
    elif front_intersect:
        front_bounce(ball, paddle)
    elif top_intersect:
        top_bounce(ball)


def ball_paddle_collision(ball, paddle):
    if ball.x_velocity < 0 and ball.pos_x > paddle.pos_x + paddle.width:
        front_intersect = front_paddle_intersect(ball, paddle.pos_x + paddle.width, paddle.pos_y, paddle.height)
    elif ball.x_velocity > 0 and ball.pos_x < paddle.pos_x:
        front_intersect = front_paddle_intersect(ball, paddle.pos_x, paddle.pos_y, paddle.height)
    else:
        front_intersect = False

    top_intersect = top_paddle_intersect(ball, paddle.pos_x, paddle.pos_y + paddle.height, paddle.width)\
                    or top_paddle_intersect(ball, paddle.pos_x, paddle.pos_y, paddle.width)

    bounce(ball, paddle, front_intersect, top_intersect)

    return front_intersect or top_intersect


def top_bottom_collision(ball, win):
    if ball.pos_y + ball.RADIUS >= win.get_height() and ball.y_velocity > 0:
        ball.y_velocity *= -1
    elif ball.pos_y - ball.RADIUS <= 0 and ball.y_velocity < 0:
        ball.y_velocity *= -1