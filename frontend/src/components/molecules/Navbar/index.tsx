import { Flex, Heading, Spacer } from "@chakra-ui/react";
import { Link } from "gatsby";
import React from "react";

const Navbar = () => {
  return (
    <Flex
      h="115px"
      w="100%"
      alignItems="center"
      bg="gray.800"
      color="white"
      px="20"
    >
      <Heading fontSize="2rem">Quantum Prisoner's Dilemma</Heading>
      <Spacer />
      <Flex w="8%" fontSize={"1.25rem"}>
        <Link to="/tutorial">Tutorial</Link>
        <Spacer />
        <Link to="/game">Game</Link>
      </Flex>
    </Flex>
  );
};

export default Navbar;
