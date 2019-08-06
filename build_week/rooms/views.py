from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class RoomsView(APIView):
    permission_classes = [IsAuthenticated]

    def index(request):
        return JsonResponse({"message": "API entrypoint.  API is stable and operating.  Please consult repository documentation for specifics on the consumption of this API.", "repository_url": "https://github.com/pymaze/backend"})

    def get(self, request):
        return JsonResponse([
            [
                {"n": 0, "e": 0, "s": 1, "w": 0,
                 "title": "Library",
                 "description": "You want weapons? Too bad, we’re in a library! Books! The most ineffective weapons in the world! Maybe try to find a sword somewhere and arm yourself!"},
                {"n": 0, "e": 1, "s": 0, "w": 0,
                 "title": "Normal hallway",
                 "description": "This is the kind of hallway you'd expect in a mildly spooky dungeon. There's moss growing on the rock walls, rivulets of water trickling out from who knows where, lit torches (with infinite fuel for some reason) in THOSE metal sconces (you know the ones I'm talking about)"},
                {"n": 0, "e": 0, "s": 1, "w": 1,
                 "title": "Joebob's hallway of many colors",
                 "description": "You step into a garishly-decorated, eye-destroyingly glittery hallway, walls encrusted with jewels of every kind and color (you can't pry them off for some reason...come on man, greedy). Is...is that a unicorn painting?"},
                {"n": 0, "e": 0, "s": 0, "w": 0,
                 "title": "Shiraz Hallway",
                 "description": "The strong, sour-sweet scent of vinegar assaults your nose as you enter this room. Sundered casks and broken bottle glass line the walls of this room. Clearly this was someone's wine cellar for a time. The shards of glass are somewhat dusty, and the spilled wine is nothing more than a sticky residue in some places. Only one small barrel remains unbroken amid the rubbish."}

            ],
            [
                {"n": 1, "e": 1, "s": 0, "w": 0,
                 "title": "The Hallway of Souls",
                 "description": "You poke your head through the break in the wall and look upon a room of titanic size. It is clearly an enormous mausoleum built to the proportions of giants. Huge niches are set into the walls within which you can discern giant bones. Stern-looking statues of stone giants stand 20 feet tall against the walls, and in the center of the room lies a 15-foot-long sarcophagus."},
                {"n": 0, "e": 0, "s": 1, "w": 1,
                 "title": "Fightclub Hallway",
                 "description": "In the center of this large room lies a 30-foot-wide round pit, its edges lined with rusting iron spikes. About 5 feet away from the pit's edge stand several stone semicircular benches. The scent of sweat and blood lingers, which makes the pit's resemblance to a fighting pit or gladiatorial arena even stronger."},
                {"n": 1, "e": 1, "s": 0, "w": 0,
                 "title": "Magik Hallway",
                 "description": "You find this chamber lit dimly by guttering candles that squat in small hills of melted wax. The smell of their smoke hits your nose along with an odor that is reminiscent of the sea. Someone has taken a large amount of salt and drawn a broad circular symbol on the floor with the candles situated equidistantly around it. Atop the salt, someone traced the symbol with a black powder that glints a dull silver in the candlelight."},
                {"n": 0, "e": 0, "s": 0, "w": 1,
                 "title": "Rikers Hall",
                 "description": "This chamber is clearly a prison. Small barred cells line the walls, leaving a 15-foot-wide pathway for a guard to walk. Channels run down either side of the path next to the cages, probably to allow the prisoners' waste to flow through the grates on the other side of the room. The cells appear empty but your vantage point doesn't allow you to see the full extent of them all."}
            ],
            [
                {"n": 0, "e": 0, "s": 1, "w": 0,
                 "title": "Hallway of Crystals",
                 "description": "You pull open the door and hear the scrape of its opening echo throughout what must be a massive room. Peering inside, you see a vast cavern. Stalactites drip down from the ceiling in sharp points while flowstone makes strange shapes on the floor."},
                {"n": 1, "e": 0, "s": 1, "w": 0,
                 "title": "Fungi Hallway",
                 "description": "This hall stinks with the wet, pungent scent of mildew. Black mold grows in tangled veins across the walls and parts of the floor. Despite the smell, it looks like it might be safe to travel through. A path of stone clean of mold wends its way through the hallway."},
                {"n": 0, "e": 0, "s": 0, "w": 0,
                 "title": "Hallway of Cremation",
                 "description": "This short hall leads to another door. On either side of the hall, niches are set into the wall within which stand clay urns. One of the urns has been shattered, and its contents have spilled onto its shelf and the floor. Amid the ash it held, you see blackened chunks of something that might be bone"},
                {"n": 0, "e": 0, "s": 0, "w": 0,
                 "title": "The Hallway of Emerald Serpents",
                 "description": "Rounded green stones set in the floor form a snake's head that points in the direction of the doorway you stand in. The body of the snake flows back and toward the wall to go round about the room in ever smaller circles, creating a spiral pattern on the floor. Similar green-stone snakes wend along the walls, seemingly at random heights, and their long bodies make wave shapes."}
            ],
            [
                {"n": 1, "e": 1, "s": 0, "w": 0,
                 "title": "The Hallway of Tattered Tapestry",
                 "description": "This room is hung with hundreds of dusty tapestries. All show signs of wear: moth holes, scorch marks, dark stains, and the damage of years of neglect. They hang on all the walls and hang from the ceiling to brush against the floor, blocking your view of the rest of the room."},
                {"n": 1, "e": 0, "s": 0, "w": 1,
                 "title": "The Hallway of Self Confrontations",
                 "description": "When looking into this chamber, you're confronted by a thousand reflections of yourself looking back. Mirrored walls set at different angles fill the room. A path seems to wind through the mirrors, although you can't tell where it leads."},
                {"n": 0, "e": 1, "s": 1, "w": 0,
                 "title": "The Hallway of Rotting Hobgoblins",
                 "description": " A huge iron cage lies on its side in this room, and its gate rests open on the floor. A broken chain lies under the door, and the cage is on a rotting corpse that looks to be a hobgoblin. Another corpse lies a short distance away from the cage. It lacks a head."},
                {"n": 0, "e": 0, "s": 0, "w": 1,
                 "title": "Arachnid Hallway",
                 "description": "Thick cobwebs fill the corners of the room, and wisps of webbing hang from the ceiling and waver in a wind you can barely feel. One corner of the ceiling has a particularly large clot of webbing within which a goblin's bones are tangled."}
            ],
        ], safe=False
        )
