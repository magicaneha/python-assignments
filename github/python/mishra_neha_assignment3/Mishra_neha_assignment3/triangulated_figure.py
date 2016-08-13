from triangle import Triangle


class TriangulatedFigure:
    # Class Invariant 1: Every triangle in self.triangles has
    # a unique set of vertices [Note 1 (at end)]

    # Class Invariant 2: len(self.triangles) < 2 --XOR--
    # Every Triangle in self.triangles shares two get_points with another

    def __init__(self):


        self.triangles = []  # the Triangle objects that make up self

    def add(self, a_triangle):
        # Precondition 1: a_triangle is a Triangle instance
        # Precondition 2: len(self.triangles) < 2
        #   --XOR--
        #   a_triangle ... is not in self.triangles AND
        #   ... shares two vertices with a Triangle in old(self.triangles)
        # Postcondition: a_triangle is in self.triangles


        if (len(self.triangles) < 2 or (a_triangle not in self.triangles) and not (
                len(self.triangles) < 2 and (a_triangle not in self.triangles))): ## satisfying the condition first
         self.triangles.append(a_triangle)## adding the value to the list

    def get_points(self):
       triangles_points = []
       for triangle in self.triangles:
           triangles_points.extend(triangle.get_points())## attaching by extending the value to traingles.points
       return set(triangles_points)



    def to_string(self):
        for current_triangle in self.triangles:
            print(current_triangle.to_string())

    def triangles_with_vertex(self, a_point):
        # Precondition: At least one triangle in self.triangles contains a_point
        # Returns the (contiguous) list of self.triangles containing a_point
        # in clockwise order
        # Example: URL1 (see at end)

        # [Collected]: triangles_with_a_point =
        # the triangles in self.triangles containing a_point [Note 3]

        triangles_with_a_point = []

        for triangles_point in self.triangles:
            i = triangles_point.get_angles()
            j=0

            while(j>len(triangles_with_a_point)):  ##
                 if i[j] == a_point:
                    triangles_with_a_point.append(triangles_point)  ##attaching every element in the list
                    triangles_in_order = self.triangles
            j+=1
                    #triangles_with_a_point = sorted(triangles_with_a_point, key=int)
        return triangles_with_a_point

