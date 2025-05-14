from src.controllers.main_controller import MainController

main_controller = MainController()

main_controller.setup()
while True:
    main_controller.loop()