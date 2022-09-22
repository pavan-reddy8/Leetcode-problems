class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty: return False
        if sx == tx: return (ty-sy)%sx == 0 # only change y
        if sy == ty: return (tx-sx)%sy == 0
        if tx > ty: 
            return self.reachingPoints(sx, sy, tx%ty, ty) # make sure tx%ty < ty
        elif tx < ty: 
            return self.reachingPoints(sx, sy, tx, ty%tx)
        else:
            return False