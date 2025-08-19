import win32com.client as wincl


if __name__ == "__main__":
  print("Welcome to RoboSpeaker 1.1")
  while True:
    x = input("Enter what you want to speak: ")
    if x == "quit":
      break
    speaker_number = 1
    spk = wincl.Dispatch("SAPI.SpVoice")
    vcs = spk.GetVoices()
    SVSFlag = 11
    print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
    spk.Voice
    spk.SetVoice(vcs.Item(speaker_number))
    spk.Speak(f"{x}")