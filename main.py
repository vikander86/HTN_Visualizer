from controller import AppController

def main():
    app = AppController()
    app.setup_initial_gui_state()
    app.run()

if __name__ == '__main__':
    main()
