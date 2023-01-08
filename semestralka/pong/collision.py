"""ball collisions"""

import numpy as np


# to assure the game is never too slow
MAX_ANGLE = np.pi / 5
# the ball gets faster each bounce
BOUNCE_INCREASE = 1.1


def front_paddle_intersect(ball, line_x, line_y, line_length):
    """intersect between front of the paddle and the ball
        calculated as intersect between line segment and circle"""

    # checks if ball isnt too far
    if abs(ball.pos_x - line_x) > ball.RADIUS:
        return False

    # intersects between cirlce and a line
    intersect1 = ball.pos_y + \
        np.sqrt(ball.RADIUS**2 - (ball.pos_x - line_x)**2)
    intersect2 = ball.pos_y - \
        np.sqrt(ball.RADIUS**2 - (ball.pos_x - line_x)**2)

    # checks if intersects are within the line segment
    if line_y <= intersect1 <= line_y + \
            line_length or line_y <= intersect2 <= line_y + line_length:
        return True
    return False


def top_paddle_intersect(ball, line_x, line_y, line_length):
    """intersect between front of the paddle and the ball
        calculated as intersect between line segment and circle"""

    # look above, same function with reversed x and y
    # i'd rather have repeating code than mixed up variables

    if abs(ball.pos_y - line_y) > ball.RADIUS:
        return False

    intersect1 = ball.pos_x + \
        np.sqrt(ball.RADIUS**2 - (ball.pos_y - line_y)**2)
    intersect2 = ball.pos_x - \
        np.sqrt(ball.RADIUS**2 - (ball.pos_y - line_y)**2)

    if line_x <= intersect1 <= line_x + \
            line_length or line_x <= intersect2 <= line_x + line_length:
        return True
    return False


def deflection_angle(ball, paddle):
    """calculates deflection angle based on distance of ball to the middle of the paddle"""

    ball_distance = paddle.pos_y + paddle.height / 2 - ball.pos_y
    relative_distance = 2 * ball_distance / paddle.height

    # it sometimes went outside of (-1, 1) so just to make sure
    if -1 < relative_distance < 1:
        return MAX_ANGLE * relative_distance
    # sign return -1 or 1 so its the max angle
    return MAX_ANGLE * np.sign(relative_distance)


def new_direction(ball, paddle):
    """calculates new velocity and angle for the ball"""

    # angle is calculated 1/2 from deflection and 1/2 from ball to x axis angle
    angle = deflection_angle(ball, paddle) + ball.angle() / 2

    # increase the velocity
    velocity = np.clip(0, ball.RADIUS, ball.total_velocity() * BOUNCE_INCREASE)

    # fancy trigonometry
    return (velocity * np.cos(angle), - velocity * np.sin(angle))


def corner_bounce(ball, paddle):
    """bounce the ball of the corner in a 45 degree angle"""

    # store the direction of the ball
    direction = - np.sign(ball.x_velocity)

    # determine the sign of the angle based on which corner was hit
    angle = np.pi / 4 * np.sign(paddle.pos_y + paddle.height / 2 - ball.pos_y)
    velocity = np.clip(0, ball.RADIUS, ball.total_velocity() * BOUNCE_INCREASE)

    ball.x_velocity = velocity * np.cos(angle) * direction
    ball.y_velocity = - velocity * np.sin(angle)


def front_bounce(ball, paddle):
    """bounce the ball of the front of the paddle"""

    direction = np.sign(ball.x_velocity)

    ball.x_velocity, ball.y_velocity = new_direction(ball, paddle)
    # always opposite x direction
    ball.x_velocity *= -direction


def top_bounce(ball, paddle):
    """bounce the ball of the top of the paddle"""

    # if ball goes up and hits top or goes down and hits bottom
    if np.sign(
            ball.y_velocity) == np.sign(
            ball.pos_y -
            paddle.pos_y +
            paddle.height /
            2):
        ball.y_velocity *= 2
    else:
        ball.y_velocity *= -1


def bounce(ball, paddle, front_intersect, top_intersect):
    """decide where to bounce the ball from"""

    if front_intersect and top_intersect and not (
            paddle.pos_y < ball.pos_y < paddle.pos_y + paddle.height):
        corner_bounce(ball, paddle)
    elif front_intersect:
        front_bounce(ball, paddle)
    elif top_intersect:
        top_bounce(ball, paddle)


def ball_paddle_collision(ball, paddle):
    """bounce the ball of the paddle if it hit"""

    if ball.x_velocity < 0 and ball.pos_x > paddle.pos_x + paddle.width:
        front_intersect = front_paddle_intersect(
            ball, paddle.pos_x + paddle.width, paddle.pos_y, paddle.height)
    elif ball.x_velocity > 0 and ball.pos_x < paddle.pos_x:
        front_intersect = front_paddle_intersect(
            ball, paddle.pos_x, paddle.pos_y, paddle.height)
    else:
        front_intersect = False

    top_intersect = \
        top_paddle_intersect(ball, paddle.pos_x, paddle.pos_y + paddle.height, paddle.width) \
        or top_paddle_intersect(ball, paddle.pos_x, paddle.pos_y, paddle.width)

    bounce(ball, paddle, front_intersect, top_intersect)

    # return true if there was collision
    return front_intersect or top_intersect


def top_bottom_collision(ball, win):
    """reverses the ball if it went out of the screen"""

    # additional conditions prevent it from getting stuck
    if ball.pos_y + ball.RADIUS >= win.get_height() and ball.y_velocity > 0:
        ball.y_velocity *= -1
    elif ball.pos_y - ball.RADIUS <= 0 and ball.y_velocity < 0:
        ball.y_velocity *= -1
