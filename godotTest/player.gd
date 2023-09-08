extends Area2D

@export var speed = 400 # Speed of the player (pixels/sec).
var screen_size # Size of game windows
signal hit

func start(pos):
	position = pos
	show()
	$CollisionShape2D.disabled = false

func _ready():
	screen_size = get_viewport_rect().size
	
func _process(_delta):
	var velocity = Vector2.ZERO
	if Input.is_action_pressed("move_right"):
		velocity.x += 1
	if Input.is_action_pressed("move_left"):
		velocity.x -= 1
	if Input.is_action_pressed("move_down"):
		velocity.y += 1
	if Input.is_action_pressed("move_up"):
		velocity.y -= 1
	
	if velocity.x != 0:
		$AnimatedSprite2D.animation = "walk"
		$AnimatedSprite2D.flip_v = false
		$AnimatedSprite2D.flip_h = velocity.x < 0
	elif velocity.y != 0:
		$AnimatedSprite2D.animation = "up"
		$AnimatedSprite2D.flip_v = velocity.y > 0
		
	if velocity.length() > 0:
		velocity = velocity.normalized() * speed
		$AnimatedSprite2D.play()
	else:
		$AnimatedSprite2D.stop()
			
	position += velocity * _delta
	position = position.clamp(Vector2.ZERO, screen_size)

func _on_body_entered(_body):
	hide()
	hit.emit()
	# Must be deferred as we can't change physics properties on a physics callback.
	$CollisionShape2D.set_deferred("disabled",true)
