# Generative AI Newsreader

## Presenting Alice, our latest AI Newsreader

## Step by Steps Manual

### Step 1: Create image of news reader personna
- Prompt: "High-quality upper body professional photo of a female media news reporter in a red coat with a newsroom background. Stunningly beautiful, radiant skin. No necklace. No malformation. Upper body and head should be fully covered in image, with blurred background behind. Realistic image. Hand should be put to table, not cross folded. Not too sexy." #AUTOMATE
- Result: saved to news_personna.jpeg #AUTOMATE

### Step 2: crawl data from news paper
- crawl_news.py 
- format output and write to file news_data #AUTOMATE

### Step 3: use open ai to generate script
- Prompt: "Create a news script, not code, that first introduces oneself as a newsreader called Alice Minh Nguyệt, and then talks about the headlines of news with points in start and give some news info. If the news is in Vietnamese, a script must be in English. Script must be readable, and no link should be included. News that are similar to each other should be read next to each other. You must classify them based on the content into 2-4 categories, then tell clearly category of each news that it belongs to. 
- News data as following to the end: {news_data}" #AUTOMATE
- Put result into file news_script #AUTOMATE

### Step 4: generate audio using ElevenLabs https://elevenlabs.io/app/speech-synthesis
- Voice: Selena
- Audio written to ElevenLabs_2024-07-05T08_48_50_Serena_pre_s50_sb75_se0_b_m2.mp3 #AUTOMATE

### Step 5: create video of body, eye and mouth movement from script and image.
- https://studio.d-id.com/video-studio #AUTOMATE 
- https://studio.d-id.com/docs
- Video save to read_finance_news.mp4 #AUTOMATE

## Step by Step Automated
(to be developed)
