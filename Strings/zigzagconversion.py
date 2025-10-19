def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        rows=['']*numRows
        current_rows,step=0,1
        for char in s:
            rows[current_rows] += char
            if current_rows==0:
                step=1
            elif current_rows==numRows-1:
                step= -1
            current_rows += step
        
        return ''.join(rows)
        
