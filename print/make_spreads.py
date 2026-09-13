import os

from weasyprint import HTML

BLOCK_COLORS = {1: "#E8552D", 2: "#2E8B8B", 3: "#7B4FBF", 4: "#C4183C", 5: "#1F7A3D"}
BLOCK_TINTS  = {1: "#FFF1EC", 2: "#E8F5F5", 3: "#F2ECFC", 4: "#FCEBEF", 5: "#E9F6EE"}
BLOCK_NAMES  = {1: "Coding", 2: "micro:bit", 3: "Electronics", 4: "3D Design", 5: "Invent"}

WEEKS = [
 dict(n=2, block=1, title="Letters Come Alive",
   goal="Your name, dancing across the screen.",
   ready=["Laptop", "Mouse", "Headphones", "Pencil"],
   steps=["Click the orange <b>Create</b> button.",
          "Click <b>Tutorials</b>. Pick <b>Animate a Name</b>. Follow it.",
          "Add every letter of your name as its own sprite.",
          "Give each letter a different sound or spin.",
          "Go back to Tutorials. Do <b>Add Effects</b> on one letter."],
   fixes=[("Letter won't change color?", "Click the letter sprite at the bottom first, not the stage."),
          ("No sound?", "Turn the volume up and check the speaker isn't muted.")],
   challenge="Animate the dog's name — or your best friend's. Make one letter do something silly.",
   sketch="Draw your name design"),

 dict(n=3, block=1, title="You're the Driver",
   goal="A sprite you steer with the arrow keys.",
   ready=["Laptop", "Mouse", "Pencil"],
   steps=["Click <b>Create</b>, then <b>Tutorials</b>.",
          "Do <b>Use Arrow Keys</b>.",
          "Try all four arrows. Fix any that go the wrong way.",
          "Go back. Do <b>Glide Around</b>.",
          "Draw a maze on the backdrop with the paint tools."],
   fixes=[("Sprite runs off screen?", "Add an <b>if on edge, bounce</b> block."),
          ("Arrows do nothing?", "Click once on the stage, then press a key.")],
   challenge="Drive your sprite from the start of the maze to the treasure without touching a wall.",
   sketch="Draw your maze"),

 dict(n=4, block=1, title="Your First Real Game",
   goal="A chase game that keeps score.",
   ready=["Laptop", "Mouse", "Pencil", "Patience"],
   steps=["Click <b>Create</b>, then <b>Tutorials</b>.",
          "Do <b>Make a Chase Game</b>. Go slow — this one is big.",
          "Find the <b>Score</b> box. Watch the number go up.",
          "Play your game three times.",
          "Swap the sprites for ones you like better."],
   fixes=[("Score never changes?", "The <b>change score by 1</b> block must sit inside the forever loop."),
          ("Chaser too fast?", "Lower the number in the <b>move</b> block.")],
   challenge="Make the score count <b>down</b> from 10 instead of up. What should happen at zero?",
   sketch="Draw your game screen"),

 dict(n=5, block=1, title="Show It Off",
   goal="A game with your name on it that other people can play.",
   ready=["Laptop", "Mouse", "A grown-up to help you share"],
   steps=["Click <b>Create</b>, then <b>Tutorials</b>.",
          "Do <b>Make a Pong Game</b>.",
          "Add a sound when the ball bounces.",
          "Add a <b>You win!</b> message at the end.",
          "Click <b>Share</b>. Copy the link."],
   fixes=[("Ball goes through the paddle?", "The <b>touching</b> block needs the paddle's exact name."),
          ("Share button missing?", "You have to be signed in to your Scratch account.")],
   challenge="Send your game to a grandparent. Then watch someone else play it — where do they get stuck?",
   sketch="Draw your winning screen"),

 dict(n=6, block=2, title="Hello, micro:bit",
   goal="A micro:bit that smiles at you.",
   ready=["Laptop", "micro:bit", "USB cable", "Pencil"],
   steps=["Plug the micro:bit into the laptop with the USB cable.",
          "Click <b>New Project</b>. Name it <b>Hello</b>.",
          "Drag a <b>show icon</b> block inside <b>on start</b>. Pick the heart.",
          "Click <b>Download</b>. Drag the file onto the <b>MICROBIT</b> drive.",
          "Unplug the cable, plug it back in. Watch the lights."],
   fixes=[("Nothing happens after the download?", "Find the <b>MICROBIT</b> drive on the laptop and drag the file right onto it."),
          ("No MICROBIT drive?", "Try the other cable. Some cables only charge \u2014 they don't carry files.")],
   challenge="Swap the heart for your initial using <b>show string</b>. Then make it flash: icon, pause, clear screen.",
   sketch="Design your own 5\u00d75 picture"),

 dict(n=7, block=2, title="Two Buttons, Two Jobs",
   goal="A micro:bit that answers you.",
   ready=["Laptop", "micro:bit", "USB cable", "Pencil"],
   steps=["Click <b>New Project</b>. Name it <b>Buttons</b>.",
          "Click <b>Input</b>. Drag out <b>on button A pressed</b>.",
          "Drop <b>show string</b> inside it. Type <b>YES</b>.",
          "Do the same for button B. Make it say <b>NO</b>.",
          "Download it. Ask the micro:bit a question."],
   fixes=[("Only one button works?", "Each button needs its own block. Check one drop-down says A and the other says B."),
          ("Words go by too fast?", "<b>show string</b> scrolls once. Press the button again.")],
   challenge="Add <b>on button A+B pressed</b>. Make it show something only you would know.",
   sketch="Write your two button messages"),

 dict(n=8, block=2, title="Shake It",
   goal="A dice you shake instead of roll.",
   ready=["Laptop", "micro:bit", "USB cable", "Pencil"],
   steps=["Click <b>New Project</b>. Name it <b>Dice</b>.",
          "Click <b>Input</b>. Drag out <b>on shake</b>.",
          "Drop <b>show number</b> inside it.",
          "Drag <b>pick random</b> from <b>Math</b> into the number slot. Make it 1 to 6.",
          "Download it. Shake it twenty times."],
   fixes=[("It rolls when you don't want it to?", "You're bumping the table. Hold it flat and shake on purpose."),
          ("Keep getting 0?", "<b>pick random</b> starts at 0. Change the first box to 1.")],
   challenge="Make it roll two dice \u2014 two numbers with a pause between. Roll twenty times. Which total wins?",
   sketch="Tally your twenty rolls"),

 dict(n=9, block=2, title="Two micro:bits Talking",
   goal="A message sent across the room with no wires.",
   ready=["Laptop", "micro:bit \u00d72", "USB cable", "Battery pack", "Pencil"],
   steps=["Click <b>New Project</b>. Name it <b>Radio</b>.",
          "Put <b>radio set group 1</b> inside <b>on start</b>.",
          "On button A pressed, add <b>radio send number 1</b>.",
          "Add <b>on radio received</b>. Put a <b>show icon</b> heart inside.",
          "Download the <b>same</b> program to <b>both</b> micro:bits. Press A."],
   fixes=[("Nothing arrives?", "Both need the same group number and the same program. Download it twice."),
          ("Only one lights up?", "The sender doesn't show its own message. Add a <b>show icon</b> under the send block too.")],
   challenge="Walk to the far end of the house and press A. How far can you get before it stops? Mark the spot.",
   sketch="Map how far the signal reached"),

 dict(n=10, block=2, title="Wear It",
   goal="A step counter you can take outside.",
   ready=["Laptop", "micro:bit", "USB cable", "Battery pack", "AAA batteries"],
   steps=["Click <b>New Project</b>. Name it <b>Steps</b>.",
          "Click <b>Variables</b>. Make a variable called <b>steps</b>.",
          "On shake, add <b>change steps by 1</b>.",
          "On button A pressed, add <b>show number steps</b>.",
          "Download it. Clip on the battery pack. Go for a walk."],
   fixes=[("Count way too high?", "One step can jiggle it twice. Walk exactly 10 steps and see what it says."),
          ("Goes blank when unplugged?", "Switch the battery pack on and push the plug all the way in.")],
   challenge="Count one lap of the garden. Then count Dad's lap. Whose legs take more steps \u2014 and why?",
   sketch="Draw where you'll wear it"),

 dict(n=11, block=3, title="Light It Up",
   goal="A light of your own that turns on and off.",
   ready=["Laptop", "micro:bit", "USB cable", "LED", "2 alligator clips", "Pencil"],
   steps=["Clip a wire from pin <b>0</b> to the LED's <b>long</b> leg.",
          "Clip a second wire from <b>GND</b> to the LED's <b>short</b> leg.",
          "In MakeCode, click <b>Advanced</b>, then <b>Pins</b>.",
          "On button A pressed, add <b>digital write pin P0 to 1</b>. Button B, make it <b>0</b>.",
          "Download it. Press A. Press B."],
   fixes=[("LED never lights?", "Turn it around. Long leg to P0, short leg to GND."),
          ("Very dim?", "Push the clips onto the bare metal legs, not the plastic.")],
   challenge="Make the light blink on its own — on, pause, off, pause, inside a <b>forever</b> loop.",
   sketch="Draw your circuit"),

 dict(n=12, block=3, title="Make Some Noise",
   goal="A micro:bit that plays a tune out loud.",
   ready=["Laptop", "micro:bit", "USB cable", "Buzzer", "2 alligator clips", "Pencil"],
   steps=["Clip a wire from pin <b>0</b> to one leg of the buzzer.",
          "Clip a second wire from <b>GND</b> to the buzzer's other leg.",
          "Click <b>Music</b>. Drag <b>start melody</b> into <b>on button A pressed</b>.",
          "Swap it for <b>play tone Middle C for 1 beat</b>. Try other notes.",
          "Download it. Press A."],
   fixes=[("No sound at all?", "Swap the two clips around, then check both grip bare metal."),
          ("Too quiet?", "Hold the buzzer flat against the table. It gets much louder.")],
   challenge="Play the first line of Happy Birthday. Write the notes down before you build it.",
   sketch="Write your tune out"),

 dict(n=13, block=3, title="The Breadboard",
   goal="A traffic light that runs by itself.",
   ready=["Laptop", "micro:bit", "Edge connector", "Breadboard", "3 LEDs", "3 resistors", "Jumper wires"],
   steps=["Push the micro:bit into the <b>edge connector</b>. Plug that into the breadboard.",
          "Put a red, a yellow and a green LED in three <b>separate</b> rows.",
          "Run a <b>220Ω resistor</b> from each short leg to the blue <b>−</b> rail.",
          "Run a jumper from <b>P0</b>, <b>P1</b> and <b>P2</b> to each long leg.",
          "Light them in order with <b>digital write</b> and <b>pause</b>. Download it."],
   fixes=[("Only one LED works?", "Each LED needs its own row. Two legs in one row is a short cut."),
          ("Nothing lights at all?", "Run one jumper from <b>GND</b> to the blue <b>−</b> rail.")],
   challenge="Time a real traffic light on your street. Change your pauses until yours matches.",
   sketch="Draw the board and the wires"),

 dict(n=14, block=3, title="Make It Move",
   goal="An arm that waves when you press a button.",
   ready=["Laptop", "micro:bit", "Edge connector", "Servo", "Jumper wires", "Cardboard + tape"],
   steps=["Plug the servo's <b>brown</b> wire to GND, <b>red</b> to 3V, <b>orange</b> to P0.",
          "Click <b>Advanced</b>, then <b>Pins</b>. Find <b>servo write pin P0 to 180</b>.",
          "Put it inside <b>on button A pressed</b>.",
          "Add another on button B. Set that one to <b>0</b>.",
          "Download it. Tape a cardboard arm to the servo. Press A."],
   fixes=[("Buzzes and shakes?", "It's pushing past its end stop. Stay between 0 and 180."),
          ("Doesn't move?", "Check the red wire is on <b>3V</b>, not GND. The colours matter.")],
   challenge="Make it wave on its own — 0, pause, 180, pause, forever. Then give it a face.",
   sketch="Draw the arm you'll tape on"),

 dict(n=15, block=3, title="Is the Plant Thirsty?",
   goal="A sensor that tells you when to water a plant.",
   ready=["Laptop", "micro:bit", "2 nails", "2 alligator clips", "A plant", "Pencil"],
   steps=["Clip a wire from <b>P1</b> to one nail, and <b>GND</b> to the other nail.",
          "Push both nails into the soil, a finger's width apart.",
          "Put <b>show number</b> → <b>analog read pin P1</b> inside <b>forever</b>.",
          "Write down the number dry. Water the plant. Write it down wet.",
          "Add an <b>if</b>: below your dry number, show a sad face."],
   fixes=[("Number jumps around?", "Normal. Pick a number halfway between your dry and wet readings."),
          ("Always says 0?", "A nail has come loose. Check both clips grip bare metal.")],
   challenge="Add the buzzer from Week 12. Make it beep until someone waters the plant.",
   sketch="Write your dry and wet numbers"),

 dict(n=16, block=4, title="Build in 3D",
   goal="Something solid you can spin around on screen.",
   ready=["Laptop", "Mouse", "Tinkercad login", "Pencil"],
   steps=["Sign in. Click <b>Create</b>, then <b>3D design</b>.",
          "Drag a <b>Box</b> onto the workplane. Pull its corners bigger.",
          "Drag a <b>Cylinder</b> in. Switch it to <b>Hole</b>. Push it into the box.",
          "Select both. Click <b>Group</b>. Watch the hole appear.",
          "Hold right-click and spin it around. Look underneath."],
   fixes=[("Hole didn't cut?", "Both shapes have to be selected before you click Group."),
          ("Shape is floating?", "Drag the little black cone on top down to zero.")],
   challenge="Build a house with a door and two windows. Every opening is a <b>Hole</b>.",
   sketch="Draw your house first"),

 dict(n=17, block=4, title="Make It Yours",
   goal="A name tag with your own name on it.",
   ready=["Laptop", "Mouse", "Tinkercad login", "Pencil"],
   steps=["Start a new <b>3D design</b>.",
          "Drag in a <b>Box</b>. Type its size: <b>60</b> by <b>20</b> by <b>3</b> mm.",
          "Drag <b>Text</b> on top. Type your name. Make it <b>2</b> mm tall.",
          "Add a <b>Cylinder</b> hole near one end for a keyring.",
          "Select everything. Click <b>Group</b>."],
   fixes=[("Letters sank into the box?", "Lift the text to 3mm. It sits on top, not inside."),
          ("Name too long?", "Make the box longer, or make the text narrower.")],
   challenge="Make one for everybody in the house. Give each person a different shape.",
   sketch="Draw the tag, full size"),

 dict(n=18, block=4, title="Measure Twice",
   goal="A stand built to fit a real object.",
   ready=["Laptop", "Mouse", "Ruler", "micro:bit", "Pencil"],
   steps=["Measure your micro:bit with a ruler. Write the mm here.",
          "Start a new design. Build a stand for it to sit in.",
          "Make the slot <b>1 mm wider</b> than you measured.",
          "Set the slot shape to <b>Hole</b>, select all, then <b>Group</b>.",
          "Spin it round. Check the slot goes all the way through."],
   fixes=[("Came out tiny?", "Tinkercad counts in mm. 5 cm is <b>50</b>."),
          ("Slot off to one side?", "Use <b>Align</b> to centre it, then nudge with the arrow keys.")],
   challenge="Design a stand for something else — a phone, a book, the dog's brush. Measure first.",
   sketch="Write your measurements in mm"),

 dict(n=19, block=4, title="Send It to the Printer",
   goal="A design on screen turned into a real object.",
   ready=["Laptop", "Mouse", "3D printer", "Slicer open", "Pencil"],
   steps=["Open your name tag from Week 17.",
          "Click <b>Export</b>, then <b>.STL</b>.",
          "Open that file in the slicer. Click <b>Slice</b>.",
          "Read the time it gives you. Write it down here.",
          "Send it to the printer. Watch the whole first layer go down."],
   fixes=[("Export greyed out?", "Click your design once to select it first."),
          ("Slicer says it's off the bed?", "Click <b>Centre</b>, then slice again.")],
   challenge="Guess the print time before the slicer tells you. How close were you?",
   sketch="My guess / the real time"),

 dict(n=20, block=4, title="Print It and Fix It",
   goal="A second version that's better than the first.",
   ready=["Laptop", "Your printed part", "3D printer", "Ruler", "Pencil"],
   steps=["Hold your print. Write down <b>three</b> things you'd change.",
          "Open the design again. Fix the worst one.",
          "Make anything thin at least <b>2 mm</b> thick.",
          "Export it and slice it again.",
          "Print it. Stand version 1 and version 2 side by side."],
   fixes=[("It snapped?", "Thin parts break. Go thicker, or lay it flat on the bed."),
          ("Letters are fuzzy?", "Raise the text a little and print it slower.")],
   challenge="Show both to someone and let them guess which came first. Ask them why.",
   sketch="Draw v1 and v2 side by side"),

 dict(n=21, block=5, title="Find a Problem",
   goal="A list of problems worth fixing.",
   ready=["This book", "Pencil", "Two people to ask"],
   steps=["Walk into every room in the house with this book.",
          "Write down <b>10 things</b> that are annoying, slow, or easy to forget.",
          "Ask two people what annoys them. Add theirs to the list.",
          "Cross out any you can't build with what's on the shelf.",
          "Circle your favourite <b>three</b>."],
   fixes=[("Can't think of anything?", "Watch someone do a boring job. Wait for the sigh."),
          ("Ideas too big?", "Shrink them. Not a robot — a light that says the dog was fed.")],
   challenge="Pick the one that helps someone else, not you. Those are the best inventions.",
   sketch="Your 10 problems"),

 dict(n=22, block=5, title="Sketch the Fix",
   goal="Three drawings, and one winner.",
   ready=["This book", "Pencil", "Someone to show"],
   steps=["Draw the problem at the top of the page.",
          "Draw <b>three different</b> machines that fix it.",
          "Label the parts of each: sensor, light, buzzer, motor.",
          "Show all three to someone. Ask which they'd use.",
          "Circle the winner. List every part you need."],
   fixes=[("Only one idea?", "Draw the lazy version, the expensive version, and the tiny version."),
          ("Can't draw?", "Boxes and arrows count. Nobody is marking the picture.")],
   challenge="Draw the silliest one too. Sometimes that's the one that works.",
   sketch="Your three ideas"),

 dict(n=23, block=5, title="Build the Ugly Version",
   goal="A rough build that actually works.",
   ready=["Laptop", "micro:bit", "Your parts list", "Cardboard + tape", "Pencil"],
   steps=["Lay every part from your list out on the table.",
          "Wire the sensor first. Get its number onto the screen.",
          "Add the thing that happens — light, sound, or servo.",
          "Hold it together with cardboard and tape. Don't make it pretty.",
          "Make it work <b>once</b>, start to finish."],
   fixes=[("Everything broken at once?", "Unplug all but the sensor. Add one part back at a time."),
          ("Worked, now it doesn't?", "A wire has moved. It is almost always a wire.")],
   challenge="Time yourself. Can you get from nothing to working in an hour? Ugly is allowed.",
   sketch="Draw how it goes together"),

 dict(n=24, block=5, title="Test It on Someone",
   goal="One real fix, found by watching someone else.",
   ready=["Your invention", "Two testers", "Pencil"],
   steps=["Hand it to someone. Say <b>nothing</b>.",
          "Write down every place they get stuck.",
          "Ask them: what did you think it would do?",
          "Fix the <b>one</b> worst thing on your list.",
          "Hand it to a second person. See if that thing is gone."],
   fixes=[("They didn't know what to do?", "That is the result. Add a label, a light, or an instruction."),
          ("It broke during the test?", "Also a result. Tape the weak part and test it again.")],
   challenge="Test it on someone younger than you. They say what adults are too polite to say.",
   sketch="Where they got stuck"),

 dict(n=25, block=5, title="Invention Night",
   goal="Your invention, shown to a room full of people.",
   ready=["Your invention", "Spare batteries", "Card for a sign", "This book"],
   steps=["Make a sign: the problem, your name, what it does.",
          "Say your demo out loud <b>three times</b> on your own first.",
          "Set it up on a table with spare batteries ready.",
          "Invite everyone. Show it. Then let them try it.",
          "Flip back through this book. All 25 weeks."],
   fixes=[("Won't work in front of people?", "Fresh batteries, and a photo of it working as back-up."),
          ("Nervous?", "Say the problem first, then show it. Thirty seconds is plenty.")],
   challenge="Teach one person one thing you learned, well enough that they can do it without you.",
   sketch="Design your sign"),
]

CSS = """
@page { size: 8.5in 5.5in; margin: 0.38in 0.42in 0.32in 0.85in; }
* { box-sizing:border-box; margin:0; padding:0; }
body { font-family:"DejaVu Sans",sans-serif; color:#1E1B1A; font-size:11.5pt; line-height:1.35; }
.page { page-break-after:always; height:4.8in; display:flex; flex-direction:column; }
.page:last-child { page-break-after:auto; }
.strip { display:flex; justify-content:space-between; align-items:center;
  border-bottom:3.5pt solid %(c)s; padding-bottom:3pt; margin-bottom:7pt; }
.block-tag { font-size:8.5pt; font-weight:bold; letter-spacing:1.6pt; color:%(c)s; text-transform:uppercase; }
.week-tag { font-size:8.5pt; font-weight:bold; letter-spacing:1.6pt; color:#8A8583; text-transform:uppercase; }
h1 { font-size:22pt; line-height:1.0; letter-spacing:-0.4pt; margin-bottom:6pt; }
.goal { background:%(t)s; border-left:5pt solid %(c)s; padding:5pt 9pt; margin-bottom:8pt; }
.goal .lbl { font-size:8pt; font-weight:bold; letter-spacing:1.2pt; color:%(c)s; text-transform:uppercase; }
.goal .txt { font-size:12pt; font-weight:bold; margin-top:2pt; }
.cols { display:flex; gap:20pt; flex:1; }
.col-ready { width:30%%; } .col-steps { width:70%%; }
h2 { font-size:8.5pt; font-weight:bold; letter-spacing:1.4pt; text-transform:uppercase; color:#8A8583; margin-bottom:6pt; }
ul { list-style:none; }
.check li { margin-bottom:6pt; font-size:11pt; padding-left:20pt; position:relative; }
.check li:before { content:""; position:absolute; left:0; top:1.5pt; width:12pt; height:12pt;
  border:1.6pt solid #1E1B1A; border-radius:2pt; }
ol.steps { list-style:none; counter-reset:s; }
ol.steps li { counter-increment:s; margin-bottom:5pt; padding-left:24pt; position:relative; font-size:11pt; }
ol.steps li:before { content:counter(s); position:absolute; left:0; top:-0.5pt; width:17pt; height:17pt;
  background:%(c)s; color:#fff; border-radius:50%%; font-size:10pt; font-weight:bold; text-align:center; line-height:17pt; }
.footrow { display:flex; gap:12pt; margin-top:6pt; align-items:stretch; }
.fix { flex:1; border:1.2pt solid #D9D4D1; border-radius:4pt; padding:6pt 9pt; }
.fix h2 { margin-bottom:4pt; }
.fix p { font-size:9pt; margin-bottom:2pt; }
.qr { width:0.95in; border:1.6pt dashed #B5AFAC; border-radius:4pt; display:flex; flex-direction:column;
  align-items:center; justify-content:center; text-align:center; padding:4pt; }
.qr .box { font-size:7pt; color:#B5AFAC; letter-spacing:0.5pt; }
.qr .cap { font-size:6.5pt; font-weight:bold; letter-spacing:0.6pt; color:#8A8583; text-transform:uppercase; margin-top:3pt; line-height:1.2; }
.yours { background:%(t)s; border-radius:5pt; padding:8pt 11pt; margin-bottom:9pt; }
.yours .lbl { font-size:8pt; font-weight:bold; letter-spacing:1.2pt; color:%(c)s; text-transform:uppercase; }
.yours .txt { font-size:12pt; margin-top:3pt; }
.sketch { flex:1; border:1.6pt solid #D9D4D1; border-radius:5pt; position:relative; margin-bottom:10pt; }
.sketch span { position:absolute; top:6pt; left:10pt; font-size:8.5pt; font-weight:bold;
  letter-spacing:1.4pt; color:#B5AFAC; text-transform:uppercase; }
.bottomrow { display:flex; gap:16pt; align-items:flex-end; }
.didit { width:34%%; }
.didit .row { display:flex; align-items:center; gap:8pt; }
.didit .bigbox { width:26pt; height:26pt; border:2pt solid %(c)s; border-radius:3pt; }
.didit .word { font-size:14pt; font-weight:bold; color:%(c)s; }
.didit .date { font-size:9pt; color:#8A8583; margin-top:6pt; }
.learned { flex:1; }
.rule { border-bottom:1.2pt solid #C9C4C1; height:17pt; }
"""

INTRO_CSS = """
@page { size: 8.5in 5.5in; margin: 0.38in 0.42in 0.32in 0.85in; }
* { box-sizing:border-box; margin:0; padding:0; }
body { font-family:"DejaVu Sans",sans-serif; color:#1E1B1A; font-size:11.5pt; line-height:1.4; }
.page { page-break-after:always; height:4.8in; display:flex; flex-direction:column; }
.page:last-child { page-break-after:auto; }
.strip { display:flex; justify-content:space-between; align-items:center; flex:0 0 auto;
  border-bottom:3.5pt solid #1E1B1A; padding-bottom:3pt; margin-bottom:10pt; }
.block-tag { font-size:8.5pt; font-weight:bold; letter-spacing:1.6pt; text-transform:uppercase; }
.week-tag { font-size:8.5pt; font-weight:bold; letter-spacing:1.6pt; color:#8A8583; text-transform:uppercase; }
h1 { font-size:30pt; line-height:1.0; letter-spacing:-0.5pt; margin-bottom:10pt; flex:0 0 auto; }
.lede { font-size:14pt; font-weight:bold; margin-bottom:4pt; flex:0 0 auto; }
.lede2 { font-size:14pt; font-weight:bold; color:#8A8583; flex:0 0 auto; }
.spacer { flex:1 1 auto; }
.name { flex:0 0 auto; border-top:1.2pt solid #C9C4C1; padding-top:10pt; font-size:11pt; color:#8A8583; }
.name .rule { display:inline-block; border-bottom:1.2pt solid #1E1B1A; width:3in; margin-left:7pt; }
.ch { display:flex; gap:9pt; margin-bottom:9pt; flex:0 0 auto; }
.ch .bar { width:5pt; border-radius:3pt; flex:0 0 auto; }
.ch .txt { flex:1; }
.ch .no { font-size:7.5pt; font-weight:bold; letter-spacing:1.2pt; text-transform:uppercase; }
.ch h2 { font-size:13pt; line-height:1.05; margin:2pt 0 3pt; }
.ch p { font-size:9.5pt; line-height:1.32; }
.real { background:#1E1B1A; color:#fff; border-radius:5pt; padding:14pt 16pt; flex:0 0 auto; }
.real h2 { font-size:16pt; margin-bottom:7pt; }
.real p { font-size:10.5pt; line-height:1.42; }
.real p + p { margin-top:7pt; }
.real .punch { font-size:12.5pt; font-weight:bold; }
"""

INTRO_CHAPTERS = [
 (1, "Weeks 1-5",   "You start on a screen",
     "A cat that walks when you tell it to. Your name, dancing. A maze you drew yourself. "
     "By Week 5 you'll have a real game, and you'll send it to somebody who doesn't live in this house."),
 (2, "Weeks 6-10",  "Then the code leaves the screen",
     "A small board with twenty-five red lights that smiles at you, answers you, and rolls dice when you shake it. "
     "In Week 9 you'll press a button and a second micro:bit across the house lights up \u2014 nothing connecting them but the air."),
 (3, "Weeks 11-15", "Then you build the circuit yourself",
     "Two clips and a bulb, and you decided where the electricity goes. Then sound. Then a traffic light running on its own. "
     "Then a micro:bit that knows the plant is thirsty before the plant does."),
 (4, "Weeks 16-20", "Then you make things you can hold",
     "You'll cut holes through shapes on screen and measure a real object so your design fits it. "
     "Then a printer turns your drawing into plastic. The first one won't be quite right \u2014 that's why there's a Week 20."),
 (5, "Weeks 21-25", "Then the instructions stop",
     "Nobody tells you what to build. You'll find ten annoying things, pick one, and build the ugly version out of cardboard and wire. "
     "In Week 25 you'll tell a room full of people what problem you solved."),
]

def intro():
    head = ('<div class="strip"><div class="block-tag">Maker Weeks</div>'
            '<div class="week-tag">Read this bit first</div></div>')
    def chunk(items):
        return "".join(
          '''<div class="ch"><div class="bar" style="background:%s"></div><div class="txt">
             <div class="no" style="color:%s">%s &middot; %s</div><h2>%s</h2><p>%s</p></div></div>'''
          % (BLOCK_COLORS[b], BLOCK_COLORS[b], wk, BLOCK_NAMES[b], h, p)
          for b, wk, h, p in items)
    return """
<div class="page">
  %(head)s
  <h1>This book is yours</h1>
  <p class="lede">Twenty-five weeks. One a week.</p>
  <p class="lede2">By the end you'll have built something nobody asked you to build.</p>
  <div class="spacer"></div>
  <div class="name">This book belongs to <span class="rule"></span></div>
</div>
<div class="page">
  %(head)s
  %(chapters_a)s
  <div class="spacer"></div>
</div>
<div class="page">
  %(head)s
  %(chapters_b)s
  <div class="spacer"></div>
  <div class="real">
    <h2>That's the part where you're doing it</h2>
    <p>A wire comes loose. The print snaps. The thing that worked on Tuesday has no interest in working on Wednesday. That isn't the part where it goes wrong.</p>
    <p class="punch">That's the part where you're actually building something.</p>
    <p>Every page in this book has an <b>If it breaks</b> box, because everybody needs one \u2014 including the people who build this stuff for a living. Find the loose wire. Fix it. Carry on.</p>
  </div>
</div>""" % dict(head=head,
                 chapters_a=chunk(INTRO_CHAPTERS[:3]),
                 chapters_b=chunk(INTRO_CHAPTERS[3:]))

def spread(w):
    b = w["block"]
    tag = "Block %d &middot; %s" % (b, BLOCK_NAMES[b])
    ready = "".join("<li>%s</li>" % x for x in w["ready"])
    steps = "".join("<li>%s</li>" % x for x in w["steps"])
    fixes = "".join("<p><b>%s</b> %s</p>" % f for f in w["fixes"])
    return """
<div class="page">
  <div class="strip"><div class="block-tag">%(tag)s</div><div class="week-tag">Week %(n)d of 25</div></div>
  <h1>%(title)s</h1>
  <div class="goal"><div class="lbl">Today you'll make</div><div class="txt">%(goal)s</div></div>
  <div class="cols">
    <div class="col-ready"><h2>Get Ready</h2><ul class="check">%(ready)s</ul></div>
    <div class="col-steps"><h2>Steps</h2><ol class="steps">%(steps)s</ol></div>
  </div>
  <div class="footrow">
    <div class="fix"><h2>If it breaks</h2>%(fixes)s</div>
    <div class="qr"><div class="box">[ QR CODE ]</div><div class="cap">Links &amp;<br>Tracker</div></div>
  </div>
</div>
<div class="page">
  <div class="strip"><div class="block-tag">%(tag)s</div><div class="week-tag">Week %(n)d &middot; Make it yours</div></div>
  <div class="yours"><div class="lbl">Your Challenge</div><div class="txt">%(challenge)s</div></div>
  <div class="sketch"><span>%(sketch)s</span></div>
  <div class="bottomrow">
    <div class="didit"><div class="row"><div class="bigbox"></div><div class="word">I DID IT!</div></div>
      <div class="date">Date: ____________________</div></div>
    <div class="learned"><h2>One thing I learned</h2><div class="rule"></div><div class="rule"></div></div>
  </div>
</div>""" % dict(tag=tag, n=w["n"], title=w["title"], goal=w["goal"],
                 ready=ready, steps=steps, fixes=fixes,
                 challenge=w["challenge"], sketch=w["sketch"])

def build(weeks, out):
    b = weeks[0]["block"]
    css = CSS % dict(c=BLOCK_COLORS[b], t=BLOCK_TINTS[b])
    html = "<!DOCTYPE html><html><head><meta charset='utf-8'><style>%s</style></head><body>%s</body></html>" % (
        css, "".join(spread(w) for w in weeks))
    HTML(string=html).write_pdf(out)
    print("wrote", out)

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    html = "<!DOCTYPE html><html><head><meta charset='utf-8'><style>%s</style></head><body>%s</body></html>" % (
        INTRO_CSS, intro())
    HTML(string=html).write_pdf(os.path.join(here, "intro.pdf"))
    print("wrote", os.path.join(here, "intro.pdf"))

    for b in sorted({w["block"] for w in WEEKS}):
        ws = [w for w in WEEKS if w["block"] == b]
        name = "block%d-weeks%d-%d.pdf" % (b, ws[0]["n"], ws[-1]["n"])
        build(ws, os.path.join(here, name))
