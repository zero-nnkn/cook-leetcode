class Solution:
    def compress(self, chars: List[str]) -> int:
        write_pos = 0
        cur_char  = chars[0]
        cur_count = 1
        chars[0] = str(cur_char)
        
        for idx, ch in enumerate(chars[1:]):
            if ch == cur_char:
                cur_count += 1
            else:
                if cur_count > 1:
                    for c in str(cur_count):
                        write_pos += 1
                        chars[write_pos] = c
                cur_char = ch
                cur_count = 1
                
                write_pos += 1
                chars[write_pos] = ch
                
        if cur_count > 1:
            write_pos += 1
            chars[write_pos] = str(cur_count)
        chars = chars[:write_pos+1]
        
        return len(chars)
        