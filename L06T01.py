from time import sleep
class TrafficLight:
    __mode = "black"

    def running(self):
        while True:

            print('\r', 'traffic_light is red', end='')
            sleep(7)
            print('\r', 'traffic_light is yellow', end='')
            sleep(2)
            print('\r', 'traffic_light is green', end='')
            sleep(7)
            print('\r', 'traffic_light is yellow', end='')
            sleep(2)

traffic_light = TrafficLight()
traffic_light.running()

##var2
        # while True:
        #
        #     light_1.running()
        #     sleep(2)
        #     light_1.hold()
        #     time.sleep(2)
        #     light_1.stop()
        #     sleep(2)

# light_1 = TrafficLight()
# light_1.running()
# light_1.hold()
# light_1.stop()

##var1
# from time import sleep
# class TrafficLight:
#     # __mode = "black"
#
#     def running(self):
#         print(f"green")
#
#     def stop(self):
#         print(f"red")
#
#     def hold(self):
#         print(f"yellow")
#
#         light_1.hold
# light_1 = TrafficLight()
# print(light_1)
# print(type(light_1))