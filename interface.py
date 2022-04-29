from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


from sutom import secret_word, all_tries

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
		self.window.color = '#000FCE'

		self.grid = GridLayout(
				cols=len(secret_word),
				rows=6,
				size_hint=(1.0,0.6)
				)
		self.window.add_widget(self.grid)

		for t in range(0, 7): #t for try
			print ("t",t)
			self.grid.clear_widgets()
			for l in range(0, 6): #l for line
				if l in range(0, t):
					print("l",l)
					for i in range(0,len(secret_word)): #i is for letter
						print("i",i)
						self.label = Label(
								text= all_tries[l][i]
							)
						self.grid.add_widget(self.label)

				elif l in range(t, 6): #l is for line
					print("l2", l)
					for d in range(t, len(secret_word)): #d is for default value(None)
						print("default")
						self.label = Label(
								text= "default",
								color= "#000FCE"
						)
						self.grid.add_widget(self.label)

			self.user_answer = TextInput(
					text='',
					multiline= False,
					size_hint= (0.4,0.1),
					font_size= 30,
					halign= 'center'
					)
			def send_text(instance):
				return self.user_answer.text
			self.user_answer.bind(on_text_validate=send_text)



		self.margin = BoxLayout(
				size_hint=(1.0, 0.1)
			)

		self.window.add_widget(self.user_answer)

		self.window.add_widget(self.margin)

		return self.window


	


if __name__ == '__main__':
	SutomGridLayout().run()