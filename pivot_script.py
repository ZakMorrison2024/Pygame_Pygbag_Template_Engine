      px,py = self.target.x,self.target.y # center point of rotation
      rel_x, rel_y = round(px - self.rect.x), round(py - self.rect.y) # find difference between target and rect coordinates
      angle = round((180/math.pi)*+math.atan2(rel_x,rel_y)) # Trignometery for rotation
      self.image = pygame.transform.rotate(self.image_clean,angle) # rotate image
