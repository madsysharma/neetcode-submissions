class HitCounter {
public:
    queue<int> hits;
    HitCounter() {
    }
    
    void hit(int timestamp) {
        hits.push(timestamp);
    }
    
    int getHits(int timestamp) {
        while(!hits.empty())
        {
            int difference = timestamp - hits.front();
            if(difference >= 300)
            {
                hits.pop();
            }
            else
            {
                break;
            }
        }
        return hits.size();
    }
};

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter* obj = new HitCounter();
 * obj->hit(timestamp);
 * int param_2 = obj->getHits(timestamp);
 */
