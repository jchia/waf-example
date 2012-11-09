#include <iostream>
#include <myproj/bar/Bar.hpp>
#include <myproj/bar/Baz.hpp>

namespace myproj {
namespace bar {

void Baz::doIt(int x) {
    Bar bar;
    std::cout << bar.calc(x) << std::endl;
}

} } // myproj::foo
