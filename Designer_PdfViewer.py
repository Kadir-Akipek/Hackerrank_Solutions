def designerPdfViewer(h, word):
    maks=0
    for i in range(len(word)):
        if(maks < h[ord(word[i])-97]):
            maks = h[ord(word[i])-97]
    return maks*len(word)