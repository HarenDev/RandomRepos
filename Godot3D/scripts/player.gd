extends CharacterBody3D

#how fast the player moves in meters per second
@export var speed = 14

#downward acceleration when in the air, in meters per second squared
@export var fall_acceleration = 75

#...
# Vertical impulse applied to the character upon jumping in meters per second.
@export var jump_impulse = 20

# 3D Vector combining speed with a direction
var target_velocity = Vector3.ZERO

# Vertical impulse applied to the character upon bouncing over a mob in
# meters per second.
@export var bounce_impulse = 16

signal hit

func _physics_process(delta):
	
	if is_on_floor() and Input.is_action_just_pressed("jump"):
		target_velocity.y = jump_impulse
	
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
	
	for index in range(get_slide_collision_count()):
		
		var collision = get_slide_collision(index)
		
		if collision.get_collider() == null:
			continue
		
		if collision.get_collider().is_in_group("mob"):
			var mob = collision.get_collider()
			
			if Vector3.UP.dot(collision.get_normal()) > 0.1:
				mob.squash()
				target_velocity.y = bounce_impulse
				
func die():
	hit.emit()
	queue_free()
	
func _on_mod_detector_body_entered(body):
	die()

func _on_player_hit():
	$MobTimer.stop()
	
