class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        current_line = []
        current_length = 0
        
        for word in words:
            # Check if adding the current word would exceed maxWidth
            if current_length + len(word) + len(current_line) > maxWidth:
                # If so, justify the current line
                if len(current_line) == 1:
                    # Special case: only one word in the line, left justify
                    result.append(current_line[0] + ' ' * (maxWidth - current_length))
                else:
                    total_spaces = maxWidth - current_length
                    space_between_words = total_spaces // (len(current_line) - 1)
                    extra_spaces = total_spaces % (len(current_line) - 1)

                    line = current_line[0]
                    for i in range(1, len(current_line)):
                        spaces = ' ' * (space_between_words + (1 if i <= extra_spaces else 0))
                        line += spaces + current_line[i]
                    
                    result.append(line)

                # Reset for the next line
                current_line = [word]
                current_length = len(word)
            else:
                # Add the word to the current line
                current_line.append(word)
                current_length += len(word)
        
        
        last_line = ' '.join(current_line)
        result.append(last_line + ' ' * (maxWidth - len(last_line)))
        
        return result

        