from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY

OUTPUT = "Alamin_Sarker_Cover_Letter_OntarioTech.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=18*mm,
    rightMargin=18*mm,
    topMargin=12*mm,
    bottomMargin=12*mm,
)

PRIMARY = colors.HexColor("#2563eb")
TEXT = colors.HexColor("#1f2937")
SECONDARY = colors.HexColor("#6b7280")

styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "Name",
    fontName="Helvetica-Bold",
    fontSize=15,
    textColor=PRIMARY,
    spaceAfter=1,
    leading=18,
)

contact_style = ParagraphStyle(
    "Contact",
    fontName="Helvetica",
    fontSize=8,
    textColor=SECONDARY,
    spaceAfter=3,
    leading=11,
)

label_style = ParagraphStyle(
    "Label",
    fontName="Helvetica-Bold",
    fontSize=8,
    textColor=PRIMARY,
    spaceAfter=3,
    spaceBefore=1,
)

body_style = ParagraphStyle(
    "Body",
    fontName="Helvetica",
    fontSize=9,
    textColor=TEXT,
    leading=13,
    spaceAfter=6,
    alignment=TA_JUSTIFY,
)

salutation_style = ParagraphStyle(
    "Salutation",
    fontName="Helvetica",
    fontSize=9,
    textColor=TEXT,
    leading=13,
    spaceAfter=6,
)

sign_style = ParagraphStyle(
    "Sign",
    fontName="Helvetica-Bold",
    fontSize=9,
    textColor=TEXT,
    leading=13,
    spaceAfter=2,
)

sign_sub_style = ParagraphStyle(
    "SignSub",
    fontName="Helvetica",
    fontSize=8,
    textColor=SECONDARY,
    leading=11,
    spaceAfter=1,
)

story = []

# Header
story.append(Paragraph("Alamin Sarker", name_style))
story.append(Paragraph(
    "alamin.sarker4241@gmail.com &nbsp;|&nbsp; +880 1740051568 &nbsp;|&nbsp; Dhaka, Bangladesh",
    contact_style
))
story.append(Paragraph(
    '<link href="https://www.linkedin.com/in/alamin-sarker-b2676522a/" color="#2563eb">'
    'linkedin.com/in/alamin-sarker-b2676522a</link> &nbsp;|&nbsp; '
    '<link href="https://github.com/AlaminSarkerFRII" color="#2563eb">github.com/AlaminSarkerFRII</link>',
    contact_style
))

story.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY, spaceAfter=5))

# Application label
story.append(Paragraph(
    "Application: MSc/PhD in Computer Science — Cybersecurity Intelligence &amp; Adversarial Systems Lab",
    label_style
))
story.append(Paragraph(
    "Faculty of Science, Ontario Tech University &nbsp;|&nbsp; Supervisor: Dr. Pooria Madani",
    contact_style
))

story.append(Spacer(1, 2*mm))

# Salutation
story.append(Paragraph("Dear Dr. Madani,", salutation_style))

# Body paragraphs
paragraphs = [
    (
        "My path into adversarial machine learning did not begin with security — it began with language. "
        "While conducting research on Bangla Entity Linking in low-resource and noisy text settings, I became "
        "increasingly preoccupied with a question that sits at the heart of your lab's work: <i>what happens when "
        "a model's assumptions about input are deliberately violated?</i> Annotation ambiguity, representation "
        "drift, and intentionally corrupted text are not just NLP challenges — they are, I came to realize, a "
        "form of adversarial pressure. That realization redirected my intellectual focus entirely."
    ),
    (
        "What my resume does not capture is the depth of that shift. Over the past year, I have been "
        "independently studying adversarial attacks on large language models — prompt injection, jailbreaking "
        "mechanics, and the structural fragility exposed by model compression. Your lab's SecRL-Prune work on "
        "reinforcement learning-guided structured pruning caught my attention precisely because it treats "
        "capability retention under compression as a security property, not just a performance metric. I find "
        "that framing genuinely compelling: the question of what a model <i>retains</i> when pruned is "
        "inseparable from what an adversary can <i>exploit</i> in that retained structure."
    ),
    (
        "I am applying for the PhD program because I want to work on problems at this level of depth. "
        "Specifically, I am drawn to your LLM-based malware mutation pipeline work. My current research requires "
        "me to reason carefully about how models generalize under distributional noise — skills I believe "
        "transfer directly to mutation-aware detection evasion, where the adversary's goal is to stay within a "
        "model's blind spots. I want to contribute to building the detection side of that arms race."
    ),
    (
        "At Technometrics Limited, I built production NLP pipelines integrating sentiment analysis and topic "
        "modeling into scalable, containerized systems. That experience gave me something graduate coursework "
        "rarely does: an understanding of where models fail under real operational conditions — edge cases, "
        "adversarial users, and data that looks nothing like training distributions. I carry that operational "
        "instinct into research."
    ),
    (
        "I am also drawn to your lab because of how you bridge academic research and professional practice. "
        "My goal is not a career that exists entirely within benchmarks. I want to do research that is legible "
        "to practitioners — work that a security operations team could act on, not just cite. Your lab's ties "
        "to real-world security operations are exactly the environment I need."
    ),
    (
        "I hold a 3.78/4.00 CGPA in Computer Science and Engineering from Bangladesh University and bring "
        "hands-on experience in Python, deep learning frameworks, and system-level tooling. More importantly, "
        "I bring a genuine intellectual commitment to understanding how and why language models break — and "
        "how to make them harder to break."
    ),
    (
        "I would be glad to discuss how my background aligns with your current projects."
    ),
]

for p in paragraphs:
    story.append(Paragraph(p, body_style))

story.append(Spacer(1, 2*mm))
story.append(Paragraph("Respectfully,", salutation_style))
story.append(Spacer(1, 1*mm))
story.append(Paragraph("Alamin Sarker", sign_style))
story.append(Paragraph("alamin.sarker4241@gmail.com", sign_sub_style))
story.append(Paragraph("+880 1740051568", sign_sub_style))

doc.build(story)
print(f"PDF generated: {OUTPUT}")
