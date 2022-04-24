from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button


#https://likegeeks.com/kivy-tutorial/#Image_in_Kivy_Button
#https://stackoverflow.com/questions/63328914/kivy-cannot-keep-focus-in-textinput-after-submiting-enter-key-does-not-confir

#exemple de calculatrice pour les layouts : https://www.geeksforgeeks.org/how-to-make-calculator-using-kivy-python/
#tuto kivy file : https://www.geeksforgeeks.org/python-kivy-kv-file/
#vidéo de tuto meuf app : https://www.youtube.com/watch?v=YDp73WjNISc&t=43s&ab_channel=PythonSimplified



class SutomGridLayout(App):
	def build(self):	
		self.window = GridLayout()
		self.window.cols = 1
		self.window.size_hint = (0.7, 0.9)
		self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

		self.grid = GridLayout(
			cols=5,
			rows=6,
			size_hint=(0.3,0.5)
			)
		self.window.add_widget(self.grid)

		self.button = Button(
			text= "BOO"
			)
		self.grid.add_widget(self.button)
		
		self.user_answer = TextInput(
			multiline= False,
			size_hint= (1,0.1),
			font_size= 30,
			halign= 'center'
			)

		self.window.add_widget(self.user_answer)


		return self.window

if __name__ == '__main__':
	SutomGridLayout().run()