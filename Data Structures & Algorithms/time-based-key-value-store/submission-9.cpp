class TimeMap {
public:
    unordered_map<string, map<int, string>> tm;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        tm[key].insert({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        auto it = tm[key].upper_bound(timestamp);
        return it == tm[key].begin() ? "" : prev(it)->second;
    }
};
