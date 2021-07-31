from glob import iglob
import re
import MeCab
import markovify

# ファイル名
file_name = "C:/work/python/src/autoComposition/2_glay.text"    

def load_from_file(files_pattern):
    # read text
    text = ""
    for path in iglob(files_pattern):
        with open(path, 'r',encoding="utf-8_sig") as f:
            text += f.read().strip()

    # delete some symbols
    unwanted_chars = ['\r', '\u3000', '-', '｜']
    for uc in unwanted_chars:
        text = text.replace(uc, '')

    # delete aozora bunko notations
    unwanted_patterns = [re.compile(r'《.*》'), re.compile(r'［＃.*］')]
    for up in unwanted_patterns:
        text = re.sub(up, '', text)

    return text


def split_for_markovify(text):
    """split text to sentences by newline, and split sentence to words by space.
    """
    # separate words using mecab
    mecab = MeCab.Tagger()
    splitted_text = ""

    # these chars might break markovify
    # https://github.com/jsvine/markovify/issues/84
    breaking_chars = [
        '(',
        ')',
        '[',
        ']',
        '"',
        "'",
    ]

    # split whole text to sentences by newline, and split sentence to words by space.
    for line in text.split():
        mp = mecab.parseToNode(line)
        while mp:
            try:
                if mp.surface not in breaking_chars:
                    splitted_text += mp.surface    # skip if node is markovify breaking char
                if mp.surface != '。' and mp.surface != '、':
                    splitted_text += ' '    # split words by space
                if mp.surface == '。':
                    splitted_text += '\n'    # reresent sentence by newline
            except UnicodeDecodeError as e:
                # sometimes error occurs
                print(line)
            finally:
                mp = mp.next

    return splitted_text


def main():
    # load text
    rampo_text = load_from_file(file_name)

    # split text to learnable form
    splitted_text = split_for_markovify(rampo_text)

    # learn model from text.
    text_model = markovify.NewlineText(splitted_text, state_size=2)

    # ... and generate from model.
    sentence = text_model.make_sentence()
    print(''.join(sentence.split()))    # need to concatenate space-splitted text

    # save learned data
    with open('learned_data.json', 'w') as f:
        f.write(text_model.to_json())

if __name__ == '__main__':
    main()