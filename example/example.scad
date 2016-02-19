rotate(a=[0, 0, 45]){
    difference(){
        cube(size=[20, 20, 20]);
        translate(v=[5, 5, -10]){
            cube(size=[10, 10, 40]);
        };
    };
};
