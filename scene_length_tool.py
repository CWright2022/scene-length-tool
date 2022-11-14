'''
Needed to find the longest scene in a play script.
Since I know what every scene begins with, I can look for that and use the line number to
determine how long each scene is (roughly)
This is a great example of me disliking the fine arts
This didn't work, however, because I actually don't know what every scene begins with.
-Cayden from the future

-Cayden Wright, 13 November 2022
'''
# file to search
import re
FILE = "c:/users/minds/downloads/FINAL PLAY SCRIPT.txt"

# regex string to match
REGEX = ".*i'm.*"


class Scene:
    __slots__ = ["start_line", "end_line", "length", "start_text"]

    def __init__(self, start_line, end_line, length, start_text):
        self.start_line = start_line
        self.end_line = end_line
        self.length = length
        self.start_text = start_text


def scene_length_key(scene):
    return scene.length


def create_scene_list(file, regex):
    '''
    scrubs through file to build a list of scenes, based on the regex input
    returns a big list
    '''
    scenes = []
    with open(file, encoding="utf-8") as file:
        have_start = False
        # eww, counting starting at 1
        count = 0
        current_line = 1
        start = 0
        end = 0
        for line in file:
            if re.match(regex, line, flags=re.IGNORECASE):
                count += 1
                if have_start:
                    end = current_line
                    length = end-start
                    scene = Scene(start, end, length, line)
                    scenes.append(scene)
                    have_start = False
                else:
                    start = current_line
                    have_start = True
            current_line += 1
        # make sure the final scene is "closed"
        end = current_line
        length = end-start
        scene = Scene(start, end, length, line)
        scenes.append(scene)
        have_start = False

    return scenes, count


def print_scenes(scenes):
    '''
    prints every scene and its info prettily
    '''
    # eww, more counting at 1
    index = 1
    for scene in scenes:
        print("POTENTIAL SCENE "+str(index)+":")
        print("LENGTH: "+str(scene.length)+" lines")
        print("BEGINS ON LINE: "+str(scene.start_line))
        print("TEXT: "+str(scene.start_text))
        print("ENDS ON LINE: "+str(scene.end_line))
        print("----------")
        index += 1


def main():
    scenes, count = create_scene_list(FILE, REGEX)
    print("found "+str(count)+" matches")
    scenes.sort(key=scene_length_key)
    print_scenes(scenes)


if __name__ == "__main__":
    main()
