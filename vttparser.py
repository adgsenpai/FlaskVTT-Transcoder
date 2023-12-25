import google.generativeai as genai

# SECRET KEY
genai.configure(api_key='SECRET_KEY')

model = genai.GenerativeModel('gemini-pro')

def openSubtitleFile(filename):
    subtitleBuffer = open(filename, 'r',encoding='utf-8')
    subtitleText = subtitleBuffer.read()
    subtitleBuffer.close()
    return subtitleText

def TranslateFile(filename,languageTo):
    subtitleText = openSubtitleFile(filename)
    PROMPT = f'''Your job is to translate the vtt file into the language {languageTo}. I just need the output file \n \n {subtitleText}'''
    # count input tokens
    print('Input tokens: ', model.count_tokens(PROMPT))
    outputBuffer = ''
    response = model.generate_content(PROMPT, stream=True,generation_config=genai.types.GenerationConfig(                        
        max_output_tokens=5000,
        temperature=1.0))        
    for chunk in response:
        print(chunk.text)  
    outputBuffer = response.text
    # output buffer to output.vtt
    outputBuffer = open('output.vtt','w')
    outputBuffer.write(outputBuffer)
    outputBuffer.close()
    return outputBuffer
 
if __name__ == '__main__':
    print('Welcome to the subtitle translator')
    filename = input('Enter the filename of the subtitle file to translate: ')
    languageTo = input('Enter the language to translate to: ')
    TranslateFile(filename,languageTo)
    print('Done translating')