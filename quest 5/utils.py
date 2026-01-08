class FishboneLine:
    def __init__(self, first_element: int) -> None:
        self.left = None
        self.center = first_element
        self.right = None

    def add_element_to_line(self, new_element: int) -> bool:
        if new_element < self.center and self.left == None:
            self.left = new_element
            return True
        elif new_element > self.center and self.right == None:
            self.right = new_element
            return True
        else:
            return False
        
    def get_left(self):
        return self.left
    
    def get_center(self):
        return self.center
    
    def get_right(self):
        return self.right

class Fishbone:
    def __init__(self, first_element: int) -> None:
        new_fishbone_line = FishboneLine(first_element)
        self.fishbone_array = [new_fishbone_line]

    def add_new_line(self, first_element: int) -> None:
        new_fishbone_line = FishboneLine(first_element)
        self.fishbone_array.append(new_fishbone_line)

    def add_element_to_fishbone(self, new_element: int) -> None:
        fishbone_lines = len(self.fishbone_array)
        for i in range(len(self.fishbone_array)):
            success = self.fishbone_array[i].add_element_to_line(new_element)
            if success: break
            elif not success and i == fishbone_lines - 1:
                self.add_new_line(new_element)

    def get_lines(self):
        return self.fishbone_array
    
    def get_lines_values(self) -> list[int]:
        lines_values = []
        for line in self.get_lines():
            line_left = str(line.get_left()) if line.get_left() else ""
            line_center = str(line.get_center())
            line_right = str(line.get_right()) if line.get_right() else ""
            
            lines_values.append(int(line_left + line_center + line_right))
            
        return lines_values

    
class SwordData:
    def __init__(self, id: int, quality: int, fishbone: Fishbone):
        self.id = id
        self.quality = quality
        self.fishbone_lines_values = fishbone.get_lines_values()

    # Used by print(sword)
    def __str__(self):
        return f"Sword #{self.id} [Q:{self.quality}] LV:{self.fishbone_lines_value}"

    # Used when you print a list of swords: print(output)
    def __repr__(self):
        return f"SwordData(id={self.id}, quality={self.quality}, linesValue={self.fishbone_lines_value})"