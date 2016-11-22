// Author Rishab Shah rishah@bu.edu
/* Copyright 2016 Rishab Shah*/
#include<iostream>
#include<fstream>
#include<map>
#include<algorithm>
#include<vector>

int main(int argc, char const *argv[]) {
    std::vector<std::string>il;
    std::ifstream f;
    f.open(argv[1]);
    std::string tmp;
    int len;
    std::string one;
    std::string in;
    int z;
    std::map<int, std::map<std::string, std::vector<std::string> > > d;
    while (f >> one) {
        tmp = one;
        sort(tmp.begin(), tmp.end());
        d[one.size()][tmp].push_back(one);
    }
    f.close();
    while (true) {
        std::vector<std::string> res;
        std::cin >> in >> z;
        if (z == 0) {
            return 0;
        }
        sort(in.begin(), in.end());
        std::map<std::string, std::vector<std::string> > :: iterator it;
        if (z == in.size()) {
            for (int i=0; i < d[z][in].size(); ++i) {
                res.push_back(d[z][in][i]);
            }
        } else {
            for (it=d[z].begin(); it != d[z].end(); ++it) {
                tmp = it->first;
                for (int i=0; i < in.size(); ++i) {
                    if (tmp[0] == in[i]) {
                        tmp.erase(0, 1);
                    }
                }
                if (tmp.size() == 0) {
                    for (int j=0; j < d[z][it->first].size(); ++j) {
                        res.push_back(d[z][it->first][j]);
                    }
                }
            }
        }
        sort(res.begin(), res.end());
        for (int i=0; i < res.size(); ++i) {
            std::cout << res[i] << std::endl;
        }
        std::cout << "." << std::endl;
    }
}

