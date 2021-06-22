from shape import Rectangle, Square
from canvas import Canvas


canvas_width = int(input(f"Please input the canvas width: "))
canvas_height = int(input(f"Please input the canvas height: "))
canvas_color = input(f"Please input the canvas color a or b: ")
canvas_color_master = {"a": (255,255,0),"b": (255,0,0)}
canvas = Canvas(canvas_width, canvas_height, color=canvas_color_master[canvas_color])



while True:
	shape = input("PLease choose the shape: rectangle or square: ")
	if shape == 'rectangle':
		r1_x = int(input(f"Please input the r1 x: "))
		r1_y = int(input(f"Please input the r1 y: "))
		r1_width = int(input(f"Please input the r1 width: "))
		r1_height = int(input(f"Please input the r1 height: "))
		r1_color = input(f"Please input the r1 color a or b: ")
		r1_color_master = {"a": (255,255,0),"b": (255,0,0)}

		r1 = Rectangle(r1_x, r1_y, r1_height, r1_width, r1_color_master[r1_color])
		r1.draw(canvas)
		

	if shape == 'square':
		s1_x = int(input(f"Please input the s1 x: "))
		s1_y = int(input(f"Please input the s1 y: "))
		s1_side = int(input(f"Please input the s1 side: "))
		s1_color = input(f"Please input the s1 color a or b: ")
		s1_color_master = {"a": (255,255,0),"b": (255,0,0)}

		s1 = Square(s1_x, s1_y, s1_side, s1_color_master[s1_color])
		s1.draw(canvas)
		
	if shape == 'quit':
		break

canvas.make('test.png')





