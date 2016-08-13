class Triangle:
    def __init__(self, three_points, two_angles):

        self.points = three_points
        self.angles = two_angles

    def has_point(self, a_point):
        # Returns whether or not a_point is a vertex of self
        for i in range(0, len(self.points)):
            if self.points[i] == a_point:  # check every element with a_point
                return True

    def point_following(self, a_point):
        if a_point == self.points[-1]:  # checking the last element  if it is equal to a_point return the first element
            return self.points[0]
        else:
            for i in range(0, len(self.points)):  # else checking other points and return the self following a_point
                if a_point == self.points[i]:
                    return self.points[i + 1]

    def point_preceding(self, a_point):
        if a_point == self.points[0]:  # checking the first element  if it is equal to a_point return the last element
            return self.points[-1]
        else:
            for i in range(0, len(self.points)):  # else checking other points and return the self following a_point
                if a_point == self.points[i]:
                    return self.points[i - 1]

    def get_angles(self):
        third = self.third_angle()
        self.angles.append(third)
        return self.angles  # simply return 3 angles of the triangle

    def get_points(self):

        return self.points  # simply return all the points

    def third_angle(self):
        third_angle = 180 - (self.angles[0] + self.angles[1])  # calculating the third angle by property
        return third_angle  # return the third angle

    def to_string(self):
        return "\nTriangle: Vertices {0}, {1}, {2}; Angles {3}, {4}, {5}" \
            .format(self.points[0], self.points[1], self.points[2],
                    self.angles[0], self.angles[1], self.third_angle())

