import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
import os


class FileOpenerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.file_chooser = FileChooserListView()
        layout.add_widget(self.file_chooser)

        open_button = Button(text='Открыть файл', size_hint=(1, 0.1))
        open_button.bind(on_press=self.open_file)
        layout.add_widget(open_button)

        return layout

    def open_file(self, instance):
        selected_file = self.file_chooser.selection
        if selected_file:
            file_path = selected_file[0]
            try:
                os.startfile(file_path)  # для Windows
            except AttributeError:
                try:
                    os.system('xdg-open "{}"'.format(file_path))  # для Linux
                except Exception as e:
                    print("Не удалось открыть файл:", e)  # для других ОС
        else:
            print("Выберите файл для открытия")


if __name__ == '__main__':
    FileOpenerApp().run()
