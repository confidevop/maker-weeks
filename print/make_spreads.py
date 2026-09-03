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
    build(WEEKS, "/home/claude/block1-weeks2-5.pdf")
