            st.session_state.board = np.array([[psi,psi,psi],[psi,psi,psi],[psi,psi,psi]])
            st.session_state.available_moves = [0,1,2,3,4,5,6,7,8,9]


        moves = st.selectbox("Make a move!",st.session_state.available_moves)

        if moves==1:
            if st.session_state.board[0,0]==psi:
                #update the value
                st.session_state.board[0,0] = get_random_value()

                # check if the user has won