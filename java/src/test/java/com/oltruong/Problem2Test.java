package com.oltruong;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

import static org.junit.jupiter.api.Assertions.assertEquals;

@ExtendWith(TimingExtension.class)
class Problem2Test {

    @Test
    void getResult() {
        assertEquals(4_613_732, Problem2.getResult());
    }
}