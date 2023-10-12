extends CharacterBody3D

#how fast the player moves in meters per second
@export var speed = 14

#downward acceleration when in the air, in meters per second squared
@export var fall_acceleration = 75

# 3D Vector combining speed with a direction
var target_velocity = Vector3.ZERO

func _physics_process(delta):
	#local variable that stores input direction
	var direction = Vector3.ZERO
	
	#X Axis Input
	if Input.is_action_pressed("move_right"):
		direction.x += 1
	if Input.is_action_pressed("move_left"):
		direction.x -= 1
		
	#Z Axis Input
	if Input.is_action_pressed("move_back"):
		direction.z += 1
	if Input.is_action_pressed("move_forward"):
		direction.z -= 1
	
	#Normalize diagonal movement	
	if direction != Vector3.ZERO:
		direction = direction.normalized()
		$Pivot.look_at(position + direction, Vector3.UP)
	
	#Ground Speed	
	target_velocity.x = direction.x * speed
	target_velocity.z = direction.z * speed
	
	#Vertical Velocity
	if not is_on_floor():
		target_velocity.y = target_velocity.y - (fall_acceleration * delta)
		
	velocity = target_velocity
	move_and_slide()

