import unreal_engine as ue
import speech_recognition as sr
class moving_up:
    def begin_play(self):
        location = self.uobject.get_actor_location()
        location.z += 100
        self.uobject.set_actor_location(location)
    def tick(self, delta_time):
        location = self.uobject.get_actor_location()
        location.z += 10 * delta_time
        self.uobject.set_actor_location(location)
       # self.uobject.call_function('PrintString', "testing", True, True, (1.0, 0.0, 0.0, 1.0), 2.0)
        #print(self.uobject.properties)
    # def on_actor_begin_overlap(self, me, other_actor): ### НЕ РАБОТАЕТ
        # location = self.uobject.get_actor_location()   ### скорее всего фиксится def begin_play(self):
        # location.z += 100                              ###                           self.uobject.bind_event('OnActorBeginOverlap', on_actor_begin_overlap)
        # self.uobject.set_actor_location(location)
class speech_recog:
    def begin_play(self):
        char = self.uobject.get_owner()
        location = char.get_actor_location()
        location.z += 100
        char.set_actor_location(location)
    def sp_rec(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            # recognize speech using Google Speech Recognition
        try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return "Could not request results from Google Speech Recognition service; {0}".format(e)
        # pass