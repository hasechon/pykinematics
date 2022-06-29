
import copy
from ntpath import join
from typing import List
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from .link_param import LinkParameter, Direction


class Robot():
    def __init__(self):
        self.components = [LinkParameter(Direction.BASE, 0, 0, 0, 0)]

    def rot(self, a, alpha, d):
        self.components.append(LinkParameter(Direction.ROT, a, alpha, d, 0))
        return self

    def liner(self, a, alpha,  theta):
        self.components.append(LinkParameter(
            Direction.LINEAR, a, alpha, 0, theta))
        return self

    def end_efecter(self, a, alpha, d, theta):
        self.components.append(LinkParameter(Direction.ROT, a, alpha, d, 0))
        return self

    def calk_fk(self, joint_variable: List) -> np.array:
        """
        関節角度を受け取って先端の位置と姿勢を返す
        処理：
            単位行列に対し、各リンクの同次変換行列をかけていく
            リンクの数だけ繰り返すと、ワールド原点から先端位置までの同時変換行列が得られる

        Args:
            joint_variable (List): 関節変数のリスト

        Returns:
            np.array: 先端位置と姿勢
        """
        fk = np.eye(4)
        for k, q in enumerate(joint_variable):
            if k == 0:
                continue
            # k-1 の座標系からkの座標系を見たときの同次変換行列を取得
            t_mat = self.transform(k-1, k)

            self.components[k]

    def get_dof(self):
        """自由度取得
        リンクの数を返す
        self.componentsはベースも含むのでn-1の値を返す
        Returns:
            int: 自由度
        """
        return len(self.components)-1

    def info(self):
        """
        リンク情報表示関数

        """
        print("{} DoF".format(len(self.components)-1))

        components_copy = copy.copy(self.components)
        components_copy.reverse()

        for i in components_copy:
            if i.direction == Direction.BASE:
                mark = "---"
            elif i.direction == Direction.LINEAR:
                mark = "||"
            elif i.direction == Direction.ROT:
                mark = " ◎ "

            print(" |  ---------------")
            print(mark, i.direction)

        print("---------------")

    def show(self, figname="fig.png") -> None:
        """show 3D model

        Args:
            figname (str, optional): file name. Defaults to "fig.png".
        """
        # init
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        # 必要な範囲だけ表示
        # ax.set_zlim(0, 10)

        # show link coordinate system
        # coordinate system of link1
        x = [0]
        y = [0]
        z = [0]
        joint_axis = [0, 0, 1]

        coodinate_0 = np.identity(3)
        print("baseのz軸は{}".format(joint_axis))
        print("zahyouは")
        print("{}".format(coodinate_0))

        for k, link in enumerate(self.components):
            print("link {} ".format(k))
            print(link)

        for k, link in enumerate(self.components):
            if k == 0:
                continue

            pre_link = self.components[k-1]
            x = [pre_link.a, link.a]
            y = [0, 1]
            z = [0, 1]
            ax.plot(x, y, z)

        # plt.show()
        plt.savefig(figname)

        return

    def update_joint_axis(self, vec, theta):
        pass

    def transform(self, pre_link_no: int, next_link_no: int) -> np.array:
        """同次変換行列 ^(i-1)T_i を計算する

        Args:
            pre_link (LinkParameter): i-1リンクのオブジェクト
            link (LinkParameter): iリンクのオブジェクト

        Returns:
            np.array: 同次変換行列
        """
        def tcos(deg):
            return np.cos(np.deg2rad(deg))

        def tsin(deg):
            return np.sin(np.deg2rad(deg))

        pre_link = self.components[pre_link_no]
        link = self.components[next_link_no]

        print(pre_link)
        print(link)

        T1 = np.array([[1, 0, 0, pre_link.a],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])

        T2 = np.array([[1, 0, 0, 0],
                       [0, tcos(pre_link.alpha), -tsin(pre_link.alpha), 0],
                       [0, tsin(pre_link.alpha), tcos(pre_link.alpha), 0],
                       [0, 0, 0, 1]])

        T3 = np.array([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, link.d],
                       [0, 0, 0, 1]])

        T4 = np.array([[tcos(link.theta), -tsin(link.theta), 0, 0],
                       [tsin(link.theta), tcos(link.theta), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])

        T12 = np.dot(T1, T2)
        T123 = np.dot(T12, T3)
        T1234 = np.dot(T123, T4)

        # print(T1)
        # print(T2)
        # print(T3)
        # print(T4)

        # print("transform matrix")
        # print(T12)
        # print(T123)
        # print(T1234)

        return T1234
