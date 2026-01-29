class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        num_rows = len(image)
        num_cols = len(image[0])
        flipped_image = []
        for row in image:
            flipped_image.append(row[::-1])
        
        for i in range(num_rows):
            for j in range(num_cols):
                if flipped_image[i][j] == 0:
                    flipped_image[i][j] = 1
                else:
                    flipped_image[i][j] = 0
        return flipped_image