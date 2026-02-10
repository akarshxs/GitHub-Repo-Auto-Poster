# ================== STREAMS ==================
import sys
sys.stdout.reconfigure(encoding="utf-8")

import time
import random
import json
import requests
import telebot
import discord
import asyncio
from io import BytesIO

TELEGRAM_BOT_TOKEN = "7778787y43rfiohreoihj3priojcrihc"
TARGET_TG_CHANNEL = "@sateichewocihewiorhc"

DISCORD_BOT_TOKEN = "MTQ3MDQ4MhbbbkjhbkhkjhkjjbhkjvcfghgchvBmhI"
DISCORD_CHANNEL_ID = 127000000000000000  # int ID

GITHUB_TOKEN = "ghp_xxxxxxxxxxxxxxxxxxx"
POST_INTERVAL = 300

# ================== STREAMS ==================
STREAMS = {
    "AI / ML / LLM": [
        "ai","machine-learning","data-science","deep-learning","computer-vision","nlp","llm","chatbot",
        "tensorflow","pytorch","openai","gpt","llama","stablediffusion","midjourney","computer-graphics",
        "big-data","data-engineering","etl","spark","hadoop","pandas","numpy","scikit-learn",
        "reinforcement-learning","robotics","nlp-tools","ai-tools","langchain","llamaindex","autogpt",
        "babyagi","crewai","agentgpt","superagi","microsoft-semantic-kernel","autogen","taskweaver",
        "metagpt","autonomous-agents","multi-agent-systems","ai-assistants","copilot","rag",
        "retrieval-augmented-generation","vector-database","pinecone","chromadb","milvus","qdrant",
        "weaviate","faiss","ollama","local-llm","quantization","gguf","prompt-engineering",
        "fine-tuning","lora","qlora","peft","huggingface","transformers","vllm","privategpt","gpt4all"
    ],

    "Cybersecurity / Hacking": [
        "cybersecurity","hacking","infosec","security-tools","penetration-testing","ethical-hacking",
        "metasploit","nmap","wireshark","burp-suite","sqlmap","aircrack-ng","owasp-zap","netcat",
        "responder","empire","cobalt-strike","bettercap","routersploit","mimikatz","impacket",
        "bloodhound","exploit-development","malware-analysis","rootkit","trojan","ransomware",
        "red-teaming","blue-teaming","bug-bounty","osint","social-engineering","fuzzing",
        "shellcode","payload","network-security","wireless-security","vulnerability-scanner",
        "reverse-engineering","software-cracking","crack","keygen","password-cracking",
        "hashcat","john-the-ripper","hydra","medusa","brute-force","rainbow-tables","cryptanalysis",
        "decompiler","disassembler","debugger","ghidra","ida-pro","ollydbg","x64dbg","radare2",
        "frida","binary-ninja","cheat-engine","game-hacking","memory-editing","obfuscation",
        "deobfuscation","drm-removal","bypass","patching","hooking","dll-injection",

        "endpoint-security","siem","soc-analyst","threat-hunting","incident-response",
        "forensics","digital-forensics","memory-forensics","disk-forensics","log-analysis",
        "zero-trust","identity-security","iam","privileged-access-management",
        "cloud-security","aws-security","azure-security","gcp-security",
        "container-security","kubernetes-security","devsecops","secure-ci-cd",
        "xdr","edr","ndr","mdr","casb","dlp","sast","dast","iast","sca",

        "heap-exploitation","stack-exploitation","format-string","use-after-free",
        "race-condition","privilege-escalation","kernel-exploits","windows-exploits",
        "linux-exploits","browser-exploitation","sandbox-escape","hypervisor-escape",
        "av-evasion","antivirus-evasion","edr-evasion","payload-obfuscation",
        "c2-infrastructure","command-and-control","covert-channels",
        "living-off-the-land","lolbins","process-injection","reflective-dll-injection",
        "apc-injection","process-hollowing","dll-sideloading","amsi-bypass","etw-bypass",

        "mobile-hacking","android-hacking","android-reversing","ios-hacking","ios-jailbreak",
        "mobile-malware","apk-analysis","ipa-analysis","frida-scripts","objection",
        "iot-security","firmware-analysis","hardware-hacking","jtag","uart",
        "side-channel-attacks","rf-hacking","bluetooth-attacks","zigbee-hacking",

        "web-security","api-security","graphql-security","oauth-attacks","jwt-attacks",
        "ssrf","xss","sqli","xxe","ssti","csrf","idor","rce","deserialization",
        "prototype-pollution","request-smuggling","http-desync",
        "cloud-exploitation","aws-pentesting","azure-pentesting","gcp-pentesting",
        "serverless-security","lambda-exploitation","s3-bucket-misconfig",

        "osint-tools","people-osint","company-osint","threat-intelligence",
        "darkweb-monitoring","brand-monitoring","leak-detection","pastebin-monitoring",
        "maltego","shodan","censys","zoomeye","hunter-io","intelx","spiderfoot",

        "malware-development","ransomware-analysis","botnet-analysis",
        "apt-research","threat-actors","campaign-tracking","yara-rules",
        "sigma-rules","snort-rules","suricata-rules","sandbox-analysis",
        "dynamic-analysis","static-analysis","reverse-malware","packer-analysis",

        "grc","risk-management","vulnerability-management",
        "security-architecture","threat-modeling","attack-surface-management",
        "nist","iso-27001","soc2","pci-dss","hipaa","gdpr","privacy-engineering"
    ],

    "Blockchain / Crypto": [
        "blockchain","crypto","fintech","trading","blockchain-games","defi","nft","solana","ethereum",
        "web3","trading-bot","crypto-bot","arbitrage-bot","mev-bot","sniper-bot","flash-loan-bot",
        "sneaker-bot","scalping-bot","grid-bot"
    ],

    "Game / XR / Metaverse": [
        "game-development","gamedev","unity","mobile-games","computer-graphics",
        "virtual-reality","augmented-reality","metaverse"
    ],
    
    "Web / Dev / Cloud": [
        "web","web-development","frontend","backend","react","vue","angular","svelte","nextjs","nodejs",
        "express","graphql","typescript","javascript","python","java","csharp","go","rust","swift",
        "flutter","dart","docker","kubernetes","devops","cloud","automation","bot","telegram-bot",
        "scraping","beautifulsoup","scrapy","crawl-spider","bot-detection","captcha-solver",
        "proxy-rotation","user-agent-spoofing","selenium","puppeteer","playwright",
        "ansible","terraform","jenkins","ci-cd","serverless","microservices"
    ],
    

    "Bots / Automation / Discord": [
        "bot","telegram-bot","discord-bot","discord-py","pycord","nextcord","disnake",
        "discord-js","discord-api","discord-music-bot","discord-moderation-bot",
        "discord-ai-bot","discord-chatbot","discord-slash-commands","discord-webhooks",
        "slack-bot","twitch-bot","whatsapp-bot","twitter-bot","reddit-bot",
        "rpa","robotic-process-automation","browser-automation","headless-browser",
        "dialogflow","rasa","botpress","voice-bot","customer-support-bot",
        "opensource","community","productivity-tools"
    ]
}

# ⚠️ Everything else in your file stays the same after this
# ================== HEADERS ==================
HEADERS = {"Accept": "application/vnd.github+json"}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"

# ================== TELEGRAM ==================
tg_bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN, parse_mode="HTML", threaded=False)

# ================== DISCORD ==================
intents = discord.Intents.default()
dc_bot = discord.Client(intents=intents)

# ================== STORAGE ==================
def load_posted():
    try:
        with open("posted.json", "r") as f:
            return set(json.load(f))
    except:
        return set()

def save_posted(data):
    with open("posted.json", "w") as f:
        json.dump(list(data), f)

posted_repos = load_posted()

# ================== GITHUB ==================
def fetch_repositories(topic):
    q = f"stars:>300 pushed:>2023-01-01 topic:{topic}"
    url = f"https://api.github.com/search/repositories?q={q}&sort=stars"
    r = requests.get(url, headers=HEADERS, timeout=20)
    r.raise_for_status()
    return r.json()["items"]

def get_github_card(repo):
    try:
        owner = repo["owner"]["login"]
        name = repo["name"]
        url = f"https://opengraph.githubassets.com/1/{owner}/{name}"
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            return r.content
    except:
        pass
    return None

# ================== FORMATS ==================
def clean_html(text):
    if not text:
        return "No description."
    return text.replace("<","").replace(">","")

def format_repo_tg(repo, stream):
    return (
        f"<b>• Repo:</b> {repo['full_name']}\n"
        f"<b>• Stream:</b> {stream}\n"
        f"<b>• Dev:</b> @AkarshxD\n"
        f"<b>━━━━━━━━━━━━━</b>\n"
        f"<b>⌯ Language:</b> {repo['language'] or 'Unknown'}\n"
        f"<b>⌯ Stars:</b> {repo['stargazers_count']} ⭐\n"
        f"<b>⌯ Forks:</b> {repo['forks_count']}\n"
        f"<b>━━━━━━━━━━━━━</b>\n"
        f"<blockquote><b>⌯ Description:</b>\n• {clean_html(repo['description'])}\n━━━━━━━━━━━━━\n"
        f"<b>⌯ GitHub Link:</b> {repo['html_url']}</blockquote>"
    )

def format_repo_discord(repo, stream):
    return (
        f"**• Repo:** {repo['full_name']}\n"
        f"**• Stream:** {stream}\n"
        f"**• Dev:** @AkarshxD\n"
        f"━━━━━━━━━━━━━\n"
        f"**⌯ Language:** {repo['language'] or 'Unknown'}\n"
        f"**⌯ Stars:** {repo['stargazers_count']} ⭐\n"
        f"**⌯ Forks:** {repo['forks_count']}\n"
        f"━━━━━━━━━━━━━\n"
        f"**⌯ Description:**\n• {repo['description']}\n"
        f"━━━━━━━━━━━━━\n"
        f"**⌯ GitHub Link:** {repo['html_url']}"
    )

# ================== SENDERS ==================
def send_telegram(image, caption):
    try:
        if image:
            tg_bot.send_photo(TARGET_TG_CHANNEL, BytesIO(image), caption=caption, parse_mode="HTML")
        else:
            tg_bot.send_message(TARGET_TG_CHANNEL, caption, parse_mode="HTML", disable_web_page_preview=True)
    except Exception as e:
        print("[TG ERROR]", e)
        tg_bot.send_message(TARGET_TG_CHANNEL, caption, parse_mode="HTML", disable_web_page_preview=True)

async def send_discord(image, caption):
    channel = dc_bot.get_channel(DISCORD_CHANNEL_ID)
    if not channel:
        return
    try:
        if image:
            file = discord.File(BytesIO(image), filename="repo.png")
            await channel.send(content=caption, file=file)
        else:
            await channel.send(content=caption)
    except Exception as e:
        print("[DC ERROR]", e)
        await channel.send(content=caption)

# ================== MAIN LOOP ==================
async def post_loop():
    await dc_bot.wait_until_ready()
    print("[BOT] Multi-Platform GitHub Repo Poster Running...")
    while True:
        try:
            stream = random.choice(list(STREAMS.keys()))
            topic = random.choice(STREAMS[stream])
            print(f"[SEARCH] {stream} → {topic}")

            repos = fetch_repositories(topic)
            random.shuffle(repos)

            for repo in repos:
                if repo["id"] in posted_repos:
                    continue

                image = get_github_card(repo)
                tg_caption = format_repo_tg(repo, stream)
                dc_caption = format_repo_discord(repo, stream)

                send_telegram(image, tg_caption)
                await send_discord(image, dc_caption)

                posted_repos.add(repo["id"])
                save_posted(posted_repos)

                print(f"[POSTED] {repo['full_name']}")
                await asyncio.sleep(POST_INTERVAL)
                break

        except Exception as e:
            print("[ERROR]", e)
            await asyncio.sleep(30)

# ================== START ==================
@dc_bot.event
async def on_ready():
    print(f"[DISCORD] Logged in as {dc_bot.user}")
    dc_bot.loop.create_task(post_loop())

dc_bot.run(DISCORD_BOT_TOKEN)
