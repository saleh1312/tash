class Tokenizer:
    def __init__(self , u_chars , limit = 20):
        self.special_tokens={"<حشو>":0 , "<مجهول>":1}
        
        self.char2id={char:idx+len(self.special_tokens) for idx, char in enumerate(u_chars)}
        self.char2id={**self.char2id,**self.special_tokens}
        
        self.id2char={v:k for k,v in self.char2id.items()}
        
        self.limit = limit
        
        
    def sent_to_ids(self , chars , pad_trunc = True):
        char_ids = [self.char2id.get(char, self.char2id["<مجهول>"] ) for char in chars]
        if pad_trunc:
            if len(char_ids) >= self.limit:
                return char_ids[:self.limit]
            
            else:
                return [ *char_ids , *[ self.char2id["<حشو>"] for i in range( self.limit - len(char_ids)) ] ] 
            
        else:
            return char_ids
         
        
    def ids_to_sent(self , ids ):
        ids_chars = [self.id2char.get(id, self.id2char[self.char2id["<مجهول>"]] ) for id in ids]
        return ids_chars
    
    