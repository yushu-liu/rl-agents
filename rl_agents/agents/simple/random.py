from rl_agents.agents.common.abstract import AbstractAgent


class RandomUniformAgent(AbstractAgent):
    def __init__(self, env, config=None):
        super(RandomUniformAgent, self).__init__(config)
        self.env = env
        self.seed()

    def act(self, state):
        return self.env.action_space.sample()

    def record(self, state, action, reward, next_state, done, info):
        pass

    def reset(self):
        pass

    def seed(self, seed=None):
        """
            Seed the rollout policy randomness source
        :param seed: the seed to be used
        :return: the used seed
        """
        return self.env.action_space.seed(seed)

    def save(self, filename):
        raise NotImplementedError()

    def load(self, filename):
        raise NotImplementedError()
